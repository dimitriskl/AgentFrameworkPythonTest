import pytest


def test_passing1():
    assert(1, 2, 3) == (1, 2, 3)

@pytest.mark.xfail()
def test_not_passing1():
    assert 1 in [2, 3, 4]

def test_passing2():
    a = 3
    b = 4
    assert(a < b)

@pytest.mark.xfail()
def test_no_passing2():
    assert "fizz" not in "fizzbuzz"

