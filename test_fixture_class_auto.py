import pytest
@pytest.fixture(scope='class',autouse=True)
def my_fixture():
    print('def my_fixture')

def test_01():
    print('def test_01')

def test_02():
    print('def test_02')

class TestA():
    def test_03(self):
        print('TestA-test_03')
    def test_04(self):
        print('TestA-test_04')


