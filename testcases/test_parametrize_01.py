import pytest


# @pytest.mark.parametrize("key", ["value"])
# def test_parametrize(key):
#     print("I'm " + key)

# 单参数，多次循环。
# 运行时将数组里的值分别赋值给变量。每赋值一次，程序运行一次
@pytest.mark.parametrize("color", ["green", "black", "white"])
def test_parametrize(color):
    assert color in ["green", "black", "white"]
    print("color is: " + color)
