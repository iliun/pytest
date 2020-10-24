# '''setup_method示例'''
# class Test_a():
#     def setup_method(self):
#         print('~~~setup_method~~~')
#     def teardown_method(self):
#         print('~~~teardown_method~~~')
#     def test_01(self):
#         print('test_01 function')
#         assert 10>11,'test_01 ERR'
#     def test_02(self):
#         print('test_02 function')
#         assert 11>10,'test_02 ERR'
'''setup_class示例'''


def setup_class(self):
    print('~~~setup_class~~~')

def teardown_class(self):
    print('~~~teardown_class~~~')
class Test_a():

    def test_01(self):
        print('test_01 function')
        assert 10>11,'test_01 ERR'
    def test_02(self):
        print('test_02 function')
        assert 11>10,'test_02 ERR'
class Test_b():
    def test_001(self):
        assert 1>2,'test_001 ERR'
# '''setup_module示例'''
# def setup_module():
#     print('~~~setup_module~~~')
# def teardown_module():
#     print('~~~teardown_module~~~')
# class Test_a():
#     def test_01(self):
#         print('test_01 function')
#         assert 10>11,'test_01 ERR'
#     def test_02(self):
#         print('test_02 function')
#         assert 11>10,'test_02 ERR'
# class Test_b():
#     def test_001(self):
#         assert 1>2,'test_001 ERR'
