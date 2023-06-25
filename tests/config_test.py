import pytest
from aioresponses import aioresponses

from config import Config


@pytest.fixture
def test_config() -> Config:
    return Config(apod_pic_service="FW6HkzJlBHzEZZnqsBuLu5K8TpGWvRpmM0Vwflx1")


@pytest.fixture
def mocked():
    with aioresponses() as m:
        yield m
