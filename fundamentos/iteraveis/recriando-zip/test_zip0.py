from zip1 import zip1


def test_empty_arg():
    assert list(zip1([])) == []


def test_no_arg():
    assert list(zip1()) == []


def test_single_iterable():
    assert list(zip1(range(3))) == [(0,), (1,), (2,)]


def test_multiple_iterables():
    assert list(zip1(range(3), range(7, 10))) == [(0, 7), (1, 8), (2, 9)]


def test_different_len_iterables():
    assert list(zip1(range(3), range(7, 17))) == [(0, 7), (1, 8), (2, 9)]

