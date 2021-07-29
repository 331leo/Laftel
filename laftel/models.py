from dataclasses import dataclass
from typing import Callable, List


@dataclass(repr=True)
class AnimeInfo:
    id: int  # Anime ID (애니 아이디)
    name: str  # Anime Title (애니 제목)
    url: str  # Anime Link (애니 링크)
    image: str  # Cover image URL (커버 사진 URL)
    content: str  # Summary of anime (애니 줄거리)
    ended: bool  # Anime complete or not (애니 완결 여부)
    awards: List[str]  # Arards that granted to anime (애니가 받은 상 목록)

    content_rating: str  # Content Rating in korean (콘텐츠 등급 - 00세 이용가)
    adultonly: bool  # Adult Content (성인인증 필요 여부)
    viewable: bool  # Available in Laftel (라프텔 시청 가능 여부)
    genres: List[str]  # Genres in korean string (장르 태그 목록)
    tags: List[str]  # Anime tags from Laftel (라프텔이 붙인 태그)

    air_year_quarter: str  # Airing quarter (방영분기 - 2020년 1분기)
    air_day: str  # Airing day (방영 요일)
    avg_rating: float  # Average User Rating out of 5 (5점 만점 중 평균 별점)

    view_male: int  # Percentage of male in total watched user (남성 시청자 비율)
    view_female: int  # Percentage of woman in total watched user (여성 시청자 비율)

    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.url = f"https://laftel.net/item/{self.id}"
        self.image = data.get("img")
        self.content = data.get("content")
        self.ended = data.get("is_ending")
        self.awards = data.get("awards")

        self.content_rating = data.get("content_rating")
        self.adultonly = data.get("is_adult")
        self.viewable = data.get("viewable")
        self.genres = data.get("genres")
        self.tags = data.get("tags")

        _animation_info = data.get("animation_info", {})
        self.air_year_quarter = _animation_info.get("air_year_quarter")
        self.air_day = (
            _animation_info.get("original_air_time")
            if _animation_info.get("original_air_time")
            else _animation_info.get("distributed_air_time")
        )

        _meta_info = data.get("meta_info", {})
        self.avg_rating = _meta_info.get("avg_rating")
        self.view_male = _meta_info.get("male")
        self.view_female = _meta_info.get("female")


@dataclass(repr=True)
class SearchResult:
    id: int  # Anime ID (애니 아이디)
    name: str  # Anime Title (애니 제목)
    url: str  # Anime Link (애니 링크)
    image: str  # Cover image URL (커버 사진 URL)
    adultonly: bool  # Adult Content (성인인증 필요 여부)
    genres: List[str]  # Genres in korean string (장르 태그 목록)

    get_data: Callable  # Function returns AnimeInfo for this anime (AnimeInfo 가져오는 함수)

    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.url = f"https://laftel.net/item/{self.id}"
        self.image = data.get("img")
        self.adultonly = data.get("is_adult")
        self.genres = data.get("genres")

    def get_data():
        """
        It Will be Filled in searchAnime Function.
        returns function "sync.getAnimeInfo" or Coroutine "getAnimeInfo".
        You will need to await this function if you had searched by coroutine.
        """
        raise NotImplementedError
