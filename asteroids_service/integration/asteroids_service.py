from aiohttp import ClientSession


class NasaApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.host = "https://api.nasa.gov"

    async def asteroid_news(self, start_date=None, end_date=None):
        async with ClientSession() as session:
            url = f"{self.host}/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
            async with session.get(url=url, params={
                "api_key": self.api_key,
                "start_date": start_date,
                "end_date": end_date,
            }) as resp:
                r = await resp.json()

        return r
