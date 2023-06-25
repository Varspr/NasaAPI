from asteroids_service.integration.asteroid import AsteroidService
from asteroids_service.service.asteroids_service import NasaAsteroid
from config import Config
from fastapi import Depends


def settings_dependency() -> Config():
    return Config()


def feed_dependency(
        config: Config = Depends(settings_dependency),
) -> NasaAsteroid:
    return NasaAsteroid(config.api_key)


def asteroid_feed_dependency(
        asteroid_service: NasaAsteroid = Depends(feed_dependency),
) -> AsteroidService:
    return AsteroidService(asteroid_service)