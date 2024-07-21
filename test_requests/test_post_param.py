import requests
import pytest


def test_mobile():
    r = requests.get('https://dict.youdao.com/keyword/key')

    result = r.json()

    assert result['MESSAGE'] == 'SUCCESS'
    assert result['CODE'] == 0
    assert r.status_code == 200
