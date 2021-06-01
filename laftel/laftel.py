from .models import AnimeInfo, SearchResult
from .utils import api_request
from typing import List
import asyncio


class ApiUrl:
    AnimeItem = "https://laftel.net/api/items/v1/{id}/"
    SearchAnime = "https://laftel.net/api/search/v1/keyword/?keyword={query}"


async def _get_AnimeInfo_by_rawdata(data: dict):
    obj = AnimeInfo(data)
    obj.url = f'https://laftel.net/item/{data.get("id", None)}'
    obj.id = data.get("id", None)
    obj.name = data.get("name", None)
    obj.image = data.get("img", None)
    obj.content = data.get("content", None)
    obj.ended = data.get("is_ending", None)
    obj.awards = data.get("awards", None)

    obj.content_rating = data.get("content_rating", None)
    obj.adultonly = data.get("is_adult", None)
    obj.viewable = data.get("viewable", None)
    obj.genres = data.get("genres", None)
    obj.tags = data.get("tags", None)

    _animation_info = data.get("animation_info", {})
    obj.air_year_quarter = _animation_info.get("air_year_quarter", None)
    obj.air_day = (
        _animation_info.get("original_air_time", None)
        if _animation_info.get("original_air_time", None)
        else _animation_info.get("distributed_air_time", None)
    )
    _meta_info = data.get("meta_info", {})
    obj.avg_rating = _meta_info.get("avg_rating", None)
    obj.view_male = _meta_info.get("male", None)
    obj.view_female = _meta_info.get("female", None)
    if not obj.id:
        return None
    return obj


async def getAnimeInfo(id: int) -> AnimeInfo:
    return await _get_AnimeInfo_by_rawdata(
        await api_request(ApiUrl.AnimeItem.format(id=id))
    )


async def searchAnime(query: str, issync: bool = False) -> List[SearchResult]:
    raw_data = await api_request(ApiUrl.SearchAnime.format(query=query))
    datas = raw_data.get("results", None)
    return_list = []
    for data in datas:

        obj = SearchResult(data)
        obj.url = f'https://laftel.net/item/{data.get("id", None)}'
        obj.id = data.get("id", None)
        obj.name = data.get("name", None)
        obj.image = data.get("img", None)
        obj.adultonly = data.get("is_adult", None)
        obj.genres = data.get("genres", None)

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
