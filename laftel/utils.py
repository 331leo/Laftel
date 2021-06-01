import aiohttp


async def api_request(RequestUrl: str):
    async with aiohttp.ClientSession(headers={"laftel": "TeJava"}) as session:
        async with session.get(RequestUrl,) as response:
            return await response.json()
