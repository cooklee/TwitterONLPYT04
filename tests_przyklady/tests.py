from math_func import add


def test_add_1_1():
    assert add(1, 1) == 2


def test_add_1_2():
    assert add(1, 2) == 3


def test_add_1_3():
    assert add(1, 3) == 5


def test_add_1_4():
    assert add(1, 4) == 5
