import pytest
@pytest.fixture(autouse=True)
def my_fixture():
    print('def my_fixture')

def test_01():
    print('def test_01')

def test_02():
    print('def test_02')
