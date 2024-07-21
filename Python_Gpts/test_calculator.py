import pytest
from calculator import Calculator


@pytest.fixture  # 作用是固定测试环境，每次执行都会返回一个Calcuator的实例
def calculator():
    return Calculator()

# # setup的写法
# class Test_Calculator:
#     def setup_method(self):
#         self.calculator = Calculator()

def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(1, -1) == 0
    assert calculator.add(-1, -1) == -2


def test_subtract(calculator):
    assert calculator.subtract(1, 2) == -1
    assert calculator.subtract(1, -1) == 2
    assert calculator.subtract(-1, -1) == 0

def test_muliply(calculator):
    assert calculator.multiply(1, 2) == 2
    assert calculator.multiply(1, -1) == -1
    assert calculator.multiply(-1, -1) == 1


def test_divide(calculator):
    assert calculator.divide(1, 2) == 0.5
    assert calculator.divide(1, -1) == -1
    assert calculator.divide(-1, -1) == 1
    with pytest.raises(ValueError):
        calculator.divide(1, 0)


if __name__ == '__main__':
    pytest.main()