import pytest
import yaml


def load_yaml():
    with open("../config/data.yaml", mode="r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_hero_name_list():
    data = load_yaml()
    expect_names = [['蒙恬', '嬴政', '王翦']]
    assert data["heroes_name_list"] == expect_names
    print(data)
    print(data["name"]["hero"])
    print(data["heroes_name"])
    print(data["heroes_name_list"])

    for names in data["heroes_name_list"]:
        for name in names:
            print(name)


if __name__ == '__main__':
    pytest.main()
