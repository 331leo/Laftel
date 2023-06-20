import aiohttp


async def api_request(RequestUrl: str):
    async with aiohttp.ClientSession(
        headers={
            "laftel": "TeJava",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_4; like Mac OS X) AppleWebKit/600.11 (KHTML, like Gecko)  Chrome/54.0.1486.383 Mobile Safari/600.8",
        }
    ) as session:
        async with session.get(
            RequestUrl,
        ) as response:
            return await response.json()
