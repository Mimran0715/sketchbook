import pytest

def func(x):
    return x + 3

def f():
    raise SystemExit(1)

class TestClass():

    def test_func():
        assert func(2) == 5

    def test_mytest():
        with pytest.raises(SystemExit):
            f()