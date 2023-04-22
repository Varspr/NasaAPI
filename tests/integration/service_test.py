import json

import pytest
from tests.config_test import mocked, test_config
from apod_service.config import ApodConfig
from apod_service.inegration.apod_service import NasaApod, ApodResponse


@pytest.fixture
def apod_api_responce() -> str:
    result = {
        "date": "2023-04-21",
        "explanation": "Along a narrow path that mostly avoided landfall, the shadow of the New Moon raced across "
                       "planet Earth's southern hemisphere on April 20 to create a rare annular-total or hybrid solar "
                       "eclipse. A mere 62 seconds of totality could be seen though, when the dark central lunar "
                       "shadow just grazed the North West Cape, a peninsula in western Australia. From top to bottom "
                       "these panels capture the beginning, middle, and end of that fleeting total eclipse phase. At "
                       "start and finish, solar prominences and beads of sunlight stream past the lunar limb. At "
                       "mid-eclipse the central frame reveals the sight only easily visible during totality and most "
                       "treasured by eclipse chasers, the magnificent corona of the active Sun. Of course eclipses "
                       "tend to come in pairs. On May 5, the next Full Moon will just miss the dark inner part of "
                       "Earth's shadow in a penumbral lunar eclipse.",
        "hdurl": "https://apod.nasa.gov/apod/image/2304/PSX_20230420_140324.jpg"
    }
    return json.dumps(result)


@pytest.fixture
def apod_api(test_config: ApodConfig) -> NasaApod:
    return NasaApod(test_config.apod_pic_service)


@pytest.mark.asyncio
async def test_apod_api(mocked, apod_api: NasaApod, apod_api_responce: list):
    mocked.get("https://api.nasa.gov/planetary/apod?api_key=FW6HkzJlBHzEZZnqsBuLu5K8TpGWvRpmM0Vwflx1",
               status=200,
               body=apod_api_responce)
    result: ApodResponse = await apod_api.picture_of_the_day("2023-04-21", hd=True)
    for item in result:
        assert isinstance(item, ApodResponse)