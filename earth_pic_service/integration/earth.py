from earth_pic_service.service.earth_pic_service import NasaEarth


class EarthService:
    def __init__(self, earth_pic_service: NasaEarth):
        self.earth_pic_service = earth_pic_service

    async def __call__(self, date: str, city: str) -> SomeResponce:
        return await self.earth_pic_service.earth_imagery(date, city)
