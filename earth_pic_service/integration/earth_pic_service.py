import asyncio
from typing import Tuple

from aiohttp import ClientSession
from geopy import Nominatim


class NasaApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.host = "https://api.nasa.gov"
        self.geolocator = Nominatim(user_agent="nasa-api")

    def city_coordinates(self, city: str) -> Tuple[float, float]:
        location = self.geolocator.geocode(city)
        return location.latitude, location.longitude

    async def earth_imagery(self, date: str, city: str) -> str:
        lat, lon = self.city_coordinates(city)
        dim = 0.025  # Дефолтное значение, рaботает - не трогай
        async with ClientSession() as session:
            url = f"{self.host}/planetary/earth/imagery?lon={lon}&lat={lat}&date={date}&dim={dim}&api_key={self.api_key}"
            async with session.get(url=url) as resp:
                res = await resp.json()
                return res["url"]

