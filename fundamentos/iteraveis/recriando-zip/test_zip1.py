import pytest

from zip1 import zip1


def test_sem_arg():
    assert list(zip1()) == []


def test_arg_vazio():
    assert list(zip1([])) == []


def test_um_iterável():
    assert list(zip1('ABC')) == [('A',), ('B',), ('C',)]


def test_vários_iteráveis():
    assert list(zip1('AB', 'xy', '01')) == [('A', 'x', '0'), ('B', 'y', '1')]


def test_iteráveis_diferentes_tamanhos():
    assert list(zip1('xy', '123')) == [('x', '1'), ('y', '2'),]


def test_vários_iteráveis_strict():
    assert list(zip1('AB', 'xy', '01', strict=True)) == [('A', 'x', '0'), ('B', 'y', '1')]


@pytest.mark.parametrize("iteráveis, msg", [
    (['AB', 'A'], 'argument 2 is shorter than argument 1'),
    (['AB', 'AB', 'A'], 'argument 3 is shorter than arguments 1-2'),
    (['A', 'AB'], 'argument 2 is longer than argument 1'),
    (['A', 'AB', 'ABC'], 'argument 2 is longer than argument 1'),
    (['A', 'A', 'AB', 'A'], 'argument 3 is longer than arguments 1-2'),
])
def test_iteráveis_diferentes_tamanhos_strict(iteráveis, msg):
    with pytest.raises(ValueError) as exc:
        list(zip1(*iteráveis, strict=True))
    assert msg in str(exc.value)
