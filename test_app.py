import pytest
from helloworld import get_message
from profile import get_profile


def test_get_message():
    assert get_message() == "Hello, World!"


def test_get_profile():
    profile = get_profile()
    assert profile["name"] == "Apichart"
    assert profile["role"] == "DevOps Engineer"


def test_profile_keys():
    profile = get_profile()
    assert "name" in profile
    assert "role" in profile