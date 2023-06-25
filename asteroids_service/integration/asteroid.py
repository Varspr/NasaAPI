from asteroids_service.service.asteroids_service import NasaAsteroid


class AsteroidService:

    def __init__(self, asteroid_feed_service: NasaAsteroid):
        self.asteroid_feed_service = asteroid_feed_service

    async def __call__(self, start_date=None, end_date=None):
        return await self.asteroid_feed_service.asteroid_news(start_date, end_date)
