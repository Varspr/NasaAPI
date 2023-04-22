import pytest
from aioresponses import aioresponses

from apod_service.config import ApodConfig


@pytest.fixture
def test_config() -> ApodConfig:
    return ApodConfig(apod_pic_service="FW6HkzJlBHzEZZnqsBuLu5K8TpGWvRpmM0Vwflx1")


@pytest.fixture
def mocked():
    with aioresponses() as m:
        yield m
