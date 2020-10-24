import pytest
class TestOrder():
    @pytest.mark.run(order=-1)
    def test_2(self):
        print('this is test2')
    def test_1(self):
        print('this is test1')
    @pytest.mark.run(order=0)
    def test_3(self):
        print('this is test3')

if __name__ == '__main__':
    pytest.main(['-q','test_order.py'])