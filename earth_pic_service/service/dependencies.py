from fastapi import Depends

from config import Config
from earth_pic_service.integration.earth import EarthService
from earth_pic_service.service.earth_pic_service import NasaEarth


def settings_dependency() -> Config:
    return Config()


def earth_dependency(
        config: Config = Depends(settings_dependency),
) -> NasaEarth:
    return NasaEarth(config.api_key)


def earth_pic_dependency(
        earth_pic_service: NasaEarth = Depends(earth_dependency),
) -> EarthService:
    return EarthService(earth_pic_service)
