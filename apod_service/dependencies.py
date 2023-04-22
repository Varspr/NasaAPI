from fastapi import Depends

from apod_service.config import ApodConfig
from apod_service.inegration.apod_service import NasaApod
from apod_service.services.apod import ApodService


def settings_dependency() -> ApodConfig:
    return ApodConfig()


def apod_dependency(
        config: ApodConfig = Depends(settings_dependency),
) -> NasaApod:
    return NasaApod(config.apod_pic_service)


def apod_pic_dependency(
        apod_pic_service: NasaApod = Depends(apod_dependency),
) -> ApodService:
    return ApodService(apod_pic_service)
