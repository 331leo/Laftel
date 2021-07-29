from .models import AnimeInfo, SearchResult
from .utils import api_request
from typing import List
import asyncio


class ApiUrl:
    AnimeItem = "https://laftel.net/api/items/v1/{id}/"
    SearchAnime = "https://laftel.net/api/search/v1/keyword/?keyword={query}"


async def getAnimeInfo(id: int) -> AnimeInfo:
    return AnimeInfo(await api_request(ApiUrl.AnimeItem.format(id=id)))


async def searchAnime(query: str, issync: bool = False) -> List[SearchResult]:
    raw_data = await api_request(ApiUrl.SearchAnime.format(query=query))
    datas = raw_data.get("results", None)
    return_list = []
    for data in datas:

        obj = SearchResult(data)

        def get_data():
            return (
                sync.getAnimeInfo(data.get("id"))
                if issync
                else getAnimeInfo(data.get("id"))
            )

        obj.get_data = get_data

        return_list.append(obj)
    return return_list


class sync:
    def getAnimeInfo(id: int, loop=asyncio.get_event_loop()) -> AnimeInfo:
        return loop.run_until_complete(getAnimeInfo(id))

    def searchAnime(query: str, loop=asyncio.get_event_loop()) -> List[SearchResult]:
        return loop.run_until_complete(searchAnime(query=query, issync=True))
