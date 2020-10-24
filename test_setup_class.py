class Test_a():
    def setup_class():
        print('~~~setup_class~~~')

    def teardown_class():
        print('~~~teardown_class~~~')
    def test_01(self):
        print('test_01 function')
        assert 12>11,'test_01 ERR'
    def test_02(self):
        print('test_02 function')
        assert 11>10,'test_02 ERR'
class Test_b():
    def test_001(self):
        assert 2>1,'test_001 ERR'