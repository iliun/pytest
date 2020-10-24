import pytest
@pytest.mark.parametrize(('a,b'),[("1+2",3),("2+3",5),("3+4",5)])
def test01(a,b):
    assert eval(a) == b