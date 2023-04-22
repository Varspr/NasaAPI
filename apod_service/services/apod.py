from apod_service.inegration.apod_service import NasaApod, ApodResponse


class ApodService:
    def __init__(self, apod_pic_service: NasaApod):
        self.apod_pic_service = apod_pic_service

    async def __call__(self, date: str, hd: bool) -> ApodResponse:
        return await self.apod_pic_service.picture_of_the_day(date, hd)
