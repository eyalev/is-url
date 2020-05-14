
from is_url import is_url


def test_true():
    assert True


def test_is_url():

    assert is_url("http://www.example.com")
    assert is_url("www.example.com")

    assert is_url("http://111 lkj") is False
