import pytest
@pytest.fixture(scope='module',autouse=True)
def my_fixture():
    print('执行my_fixture')



class Test_b():
    def test_001(self):
        print('Test_b')
        assert 3>2,'test_001 ERR'
    def test_002(self):
        print('test_002')

@pytest.mark.usefixtures('my_fixture')
class Test_c():
    def test_001(self):
        print('in Test_c test_001')

    def test_002(self):
        print('in Test_c test_002')