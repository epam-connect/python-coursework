import pytest
import sys
from func.add import add

@pytest.mark.skip
def test_add1():
    assert add(5, 10) == 15

@pytest.mark.skipif(sys.version_info > (3,0), reason="Python version >= 3.0 satisfied")
def test_add2():
    assert add(5, 10) == 15
    raise Exception("Python version <= 3.0")


@pytest.mark.xfail(sys.platform == 'win32', reason="Allowed to fail in windows")
def test_add3():
    assert add(5, 10) == 15
    raise Exception

@pytest.mark.addition
@pytest.mark.parametrize(
    "inp1, inp2, output",
    [
        (1, 2, 3),
        (10, 5, 15),
        (18, 20, 38)
    ],
    ids=["test1", "test2", "test3"]
)
def test_add4(inp1, inp2, output):
    assert add(inp1, inp2) == output