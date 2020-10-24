import pytest
@pytest.fixture()
def my_fixture():
    print('def my_fixture')
#调用方式1
def test_01(my_fixture):
    print('def test_01')
#调用方式2
@pytest.mark.usefixtures('my_fixture')
def test_02():
    print('def test_02')
