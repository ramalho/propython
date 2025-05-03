import pytest

from zip0 import zip0


def test_empty_arg():
    assert list(zip0([])) == []


def test_no_arg():
    assert list(zip0()) == []


def test_single_iterable():
    assert list(zip0(range(3))) == [(0,), (1,), (2,)]


def test_multiple_iterables():
    assert list(zip0(range(3), range(7, 10))) == [(0, 7), (1, 8), (2, 9)]


def test_different_len_iterables():
    assert list(zip0(range(3), range(7, 17))) == [(0, 7), (1, 8), (2, 9)]


@pytest.mark.parametrize("iterables, msg", [
    ([range(1), range(2)], 'argument 2 is longer than argument 1'),
    ([range(1), range(2), range(3)], 'argument 2 is longer than argument 1'),
    # ([range(1), range(1), range(2), range(1)], 'argument 3 is longer than arguments 1-2'),
    #([range(2), range(1)], 'argument 2 is shorter than argument 1'),
    #([range(2), range(2), range(1)], 'argument 3 is shorter than arguments 1-2'),
])
def test_different_len_iterables_strict(iterables, msg):
    with pytest.raises(ValueError) as exc:
        list(zip0(*iterables, strict=True))
    assert msg in str(exc.value)