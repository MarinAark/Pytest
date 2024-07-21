import pytest
from reverse_string import reverse_string


@pytest.fixture
def setup():
    print("测试开始")


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("abc") == "cba"


if __name__ == '__main__':
    pytest.main()

