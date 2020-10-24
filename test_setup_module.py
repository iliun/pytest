'''setup_module示例'''
def setup_module():
    print('~~~setup_module~~~')
def teardown_module():
    print('~~~teardown_module~~~')
class Test_a():
    def test_01(self):
        print('test_01 function')
        assert 12>11,'test_01 ERR'
    def test_02(self):
        print('test_02 function')
        assert 11>10,'test_02 ERR'
class Test_b():
    def test_001(self):
        assert 3>2,'test_001 ERR'