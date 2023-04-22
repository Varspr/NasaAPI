
from aiohttp import ClientSession

from pydantic import BaseModel


class ApodResponse(BaseModel):
    date: str
    explanation: str
    hdurl: str


class NasaApod:
    def __init__(self, api_key: str):
        self.api_url = "https://api.nasa.gov"
        self.api_key = api_key

    async def picture_of_the_day(self, date: str, hd: bool) -> ApodResponse:
        async with ClientSession() as session:
            url = f"{self.api_url}/planetary/apod?api_key={self.api_key}"
            async with session.get(url, params={"api_key": self.api_key,
                                                "date": date,
                                                "hd": str(hd).lower()}) as resp:
                res = await resp.json()

                return ApodResponse(date=res["date"], explanation=res["explanation"], hdurl=res["hdurl"])


