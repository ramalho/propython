from zip0 import zip0


def test_sem_arg():
    assert list(zip0()) == []


def test_arg_vazio():
    assert list(zip0([])) == []


def test_um_iterável():
    assert list(zip0('ABC')) == [('A',), ('B',), ('C',)]


def test_vários_iteráveis():
    assert list(zip0('AB', 'xy', '01')) == [('A', 'x', '0'), ('B', 'y', '1')]


def test_iteráveis_diferentes_tamanhos():
    assert list(zip0('xy', '123')) == [('x', '1'), ('y', '2'),]

