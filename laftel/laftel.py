from .models import AnimeInfo, SearchEpisode, SearchResult, SeriesSearchResult
from .utils import api_request
from typing import List
import asyncio


class ApiUrl:
    AnimeItem = "https://laftel.net/api/items/v2/{id}/"
    SearchAnime = "https://laftel.net/api/search/v3/keyword/?keyword={query}"
    SearchSeries = "https://laftel.net/api/items/v2/series/{id}/?limit=50&offset=0"
    SearchEpisodes = "https://laftel.net/api/episodes/v2/list/?item_id={id}&sort=oldest&limit=50&show_playback_offset=true&offset=0"


async def getAnimeInfo(id: int) -> AnimeInfo:
    return AnimeInfo(await api_request(ApiUrl.AnimeItem.format(id=id)))


async def searchSeries(id: int) -> List[SeriesSearchResult]:
    return [
        SeriesSearchResult(data)
        for data in (await api_request(ApiUrl.SearchSeries.format(id=id))).get(
            "results"
        )
    ]


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


async def searchEpisodes(id: int) -> List[SearchEpisode]:
    return [
        SearchEpisode(data)
        for data in (await api_request(ApiUrl.SearchEpisodes.format(id=id))).get(
            "results"
        )
    ]


class sync:
    def getAnimeInfo(id: int, loop=asyncio.get_event_loop()) -> AnimeInfo:
        return loop.run_until_complete(getAnimeInfo(id))

    def searchAnime(query: str, loop=asyncio.get_event_loop()) -> List[SearchResult]:
        return loop.run_until_complete(searchAnime(query=query, issync=True))

    def searchSeries(
        id: int, loop=asyncio.get_event_loop()
    ) -> List[SeriesSearchResult]:
        return loop.run_until_complete(searchSeries(id=id))

    def searchEpisodes(id: int, loop=asyncio.get_event_loop()) -> List[SearchEpisode]:
        return loop.run_until_complete(searchEpisodes(id=id))
