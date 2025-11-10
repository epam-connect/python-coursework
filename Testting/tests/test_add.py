from func.add import add, add_integers
import pytest

def test_add1():
    assert add(2, 3) == 5

def test_add2():
    assert add("a", "b") == "ab"

def test_add_integers1():
    assert add_integers(5, 10) == 15

def test_add_integers():
    with pytest.raises(ValueError, match="a, b both should be integers") as exe:
        assert add_integers("a", "b") == "ab"
