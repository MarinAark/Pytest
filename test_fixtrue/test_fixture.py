import pytest


@pytest.fixture(autouse=True)
def func():
    print("测试前置")


# pytest模块，文件名要以test_开头，函数也要以test开头
def teardown_class():
    print("结束测试")


def setup_class():
    print("开始测试")


class TestOne:

    def test_one(func):
        expect = 1
        actual = 1
        assert expect == actual

    def test_two(self):
        expect = 2
        actual = 1
        assert expect != actual

    def test_three(self):
        expect = 3
        actual = 3
        assert expect == actual
        assert 1 < 2
        assert 1 <= 1
        assert 1 == 1
        assert 2 > 1
        assert 2 >= 2
        assert 1 != 2
        assert 'a' in 'abc'
        assert 'a' not in 'bcd'
        assert True is True
        assert True is not False


if __name__ == '__main__':
    pytest.main()
