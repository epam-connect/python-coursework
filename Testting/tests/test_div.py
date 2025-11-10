import pytest

def test_div():
    with pytest.raises(ZeroDivisionError):
        a = 1 / 0

def test_div2():
    with pytest.raises(ZeroDivisionError):
        a = 1 / 0