import pytest

from zip1 import zip1


def test_empty_arg():
    assert list(zip1([])) == []


def test_no_arg():
    assert list(zip1()) == []


def test_single_iterable():
    assert list(zip1(range(3))) == [(0,), (1,), (2,)]


def test_multiple_iterables():
    assert list(zip1(range(3), range(7, 10))) == [(0, 7), (1, 8), (2, 9)]


def test_multiple_iterables_strict():
    assert list(zip1(range(3), range(7, 10), strict=True)) == [(0, 7), (1, 8), (2, 9)]


def test_different_len_iterables():
    assert list(zip1(range(3), range(7, 17))) == [(0, 7), (1, 8), (2, 9)]


@pytest.mark.parametrize("iterables, msg", [
    ([range(2), range(1)], 'argument 2 is shorter than argument 1'),
    ([range(2), range(2), range(1)], 'argument 3 is shorter than arguments 1-2'),
    ([range(1), range(2)], 'argument 2 is longer than argument 1'),
    ([range(1), range(2), range(3)], 'argument 2 is longer than argument 1'),
    ([range(1), range(1), range(2), range(1)], 'argument 3 is longer than arguments 1-2'),
])
def test_different_len_iterables_strict(iterables, msg):
    with pytest.raises(ValueError) as exc:
        list(zip1(*iterables, strict=True))
    assert msg in str(exc.value)