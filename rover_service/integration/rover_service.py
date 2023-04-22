import asyncio
from typing import Any, Coroutine

import aiohttp

from aiohttp import ClientSession


class NasaApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.host = "https://api.nasa.gov"

    async def my_request(self, url: str):
        async with ClientSession() as session:
            async with session.get(url=url) as resp:
                return await resp.json()

    async def get_many(self):
        sol: int = 1000
        front_camera: str = "FHAZ"
        page: int = 1
        date = "2015-01-01"
        tasks = [
            self.my_request(f"{self.host}/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={self.api_key}"),
            self.my_request(
                f"{self.host}/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&camera={front_camera}&api_key={self.api_key}"),
            self.my_request(
                f"{self.host}/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&page={page}&api_key={self.api_key}"),
            self.my_request(
                f"{self.host}/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={self.api_key}")]
        results = asyncio.gather(*tasks)
        # results = [response1, response2, response3, response4]
        return results

    async def rover_call(self):
        r = await self.get_many()
        return await r


