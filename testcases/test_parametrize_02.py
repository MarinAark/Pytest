import pytest


# 使用数组的形式
@pytest.mark.parametrize("name, word", [["张三", "法外狂徒"], ["李四", "法外施恩"]])
def test_parametrize(name, word):
    print(f'{name}的台词是：{word}')


# 使用元组的形式
@pytest.mark.parametrize("name, word", [("张三", "法外狂徒"), ("李四", "法外施恩")])
def test_parametrize(name, word):
    print(f'{name}的台词是：{word}')
