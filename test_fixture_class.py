import pytest
@pytest.fixture(scope='class')
def my_fixture():
    print('def my_fixture')

def test_01():
    print('def test_01')

def test_02():
    print('def test_02')
@pytest.mark.usefixtures('my_fixture')
class TestA():
    def test_03(self):
        print('TestA-test_03')
    def test_04(self):
        print('TestA-test_04')

class TestB():
    def test_05(self):
        print('TestB-test_05')
    def test_06(self):
        print('TestB-test_06')

