import pytest
class TestGroup():
    @pytest.mark.smoke
    @pytest.mark.p0
    def test_2(self):
        print('this is test2')

    def test_1(self):
        print('this is test1')
    @pytest.mark.smoke
    def test_3(self):
        print('this is test3')
