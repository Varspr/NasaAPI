from fastapi import Depends

from config import Config
from apod_service.services.apod_service import NasaApod
from apod_service.inegration.apod import ApodService


def settings_dependency() -> Config:
    return Config()


def apod_dependency(
        config: Config = Depends(settings_dependency),
) -> NasaApod:
    return NasaApod(config.api_key)


def apod_pic_dependency(
        apod_pic_service: NasaApod = Depends(apod_dependency),
) -> ApodService:
    return ApodService(apod_pic_service)
