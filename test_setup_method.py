'''setup_method示例'''
class Test_a():
    def setup_method(self):
        print('~~~setup_method~~~')
    def teardown_method(self):
        print('~~~teardown_method~~~')
    def test_01(self):
        print('test_01 function')
        assert 12>11,'test_01 ERR'
    def test_02(self):
        print('test_02 function')
        assert 10>10,'test_02 ERR'