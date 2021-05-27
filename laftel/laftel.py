from .objects import AnimeInfo, SearchResult
from .utils import api_request
import asyncio


class ApiUrl:
    AnimeItem = "https://laftel.net/api/items/v1/{id}/"
    SearchAnime = "https://laftel.net/api/search/v1/keyword/?keyword={query}"


async def _get_AnimeInfo_by_rawdata(data: dict):
    obj = AnimeInfo(data)
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
    obj.air_time = (
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


async def get_AnimeInfo(id: int):
    return await _get_AnimeInfo_by_rawdata(
        await api_request(ApiUrl.AnimeItem.format(id=id))
    )


async def search_Anime(query: str, issync: bool = False):
    raw_data = await api_request(ApiUrl.SearchAnime.format(query=query))
    datas = raw_data.get("results", None)
    return_list = []
    for data in datas:

        obj = SearchResult(data)
        obj.id = data.get("id", None)
        obj.name = data.get("name", None)
        obj.image = data.get("img", None)
        obj.adultonly = data.get("is_adult", None)
        obj.genres = data.get("genres", None)

        def get_data():
            return (
                sync.get_AnimeInfo(data.get("id"))
                if issync
                else get_AnimeInfo(data.get("id"))
            )

        obj.get_data = get_data

        return_list.append(obj)
    return return_list


class sync:
    def get_AnimeInfo(id: int, loop=asyncio.get_event_loop()):
        return loop.run_until_complete(get_AnimeInfo(id))

    def search_Anime(query: str, loop=asyncio.get_event_loop()):
        return loop.run_until_complete(search_Anime(query=query, issync=True))
