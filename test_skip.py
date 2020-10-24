import pytest
class TestOrder():

    def test_2(self):
        print('this is test2')
    @pytest.mark.skip(reason=' skip test_1~~~')
    def test_1(self):
        print('this is test1')
    a = 1
    b = 2
    @pytest.mark.skipif(a<b,reason='skip test_3 if a<b~~')
    def test_3(self):
        print('this is test3')

if __name__ == '__main__':
    pytest.main(['-q','test_order.py'])