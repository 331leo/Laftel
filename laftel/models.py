from dataclasses import dataclass
from typing import Callable, List, Optional


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

    air_year_quarter: Optional[str]  # Airing quarter (방영분기 - 2020년 1분기)
    air_day: Optional[str]  # Airing day (방영 요일)
    avg_rating: float  # Average User Rating out of 5 (5점 만점 중 평균 별점)

    series_id: Optional[int]  # Series ID (시리즈 아이디)
    production: Optional[str]  # Production company (제작사)

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
        self.viewable = data.get("is_viewing")
        self.genres = data.get("genres")
        self.tags = data.get("tags")

        self.air_year_quarter = data.get("air_year_quarter", "")
        self.air_day = data.get("distributed_air_time", "")

        self.avg_rating = data.get("avg_rating")

        self.series_id = data.get("series_id", None)
        self.production = data.get("production", "")


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


@dataclass(repr=True)
class SeriesSearchResult:
    id: int  # Anime ID (애니 아이디)
    name: str  # Anime Title (애니 제목)

    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")


@dataclass(repr=True)
class SearchEpisode:
    id: str  # Episode ID (에피소드 아이디)
    title: str  # Anime Title (애니 제목)
    subject: str  # Episode Title (에피소드 제목)
    description: str  # Episode Description (에피소드 설명)
    episode_num: str  # Episode Number (에피소드 번호)
    episode_order: int  # Episode Order (에피소드 순서)
    thumbnail_path: str  # Thumbnail URL (썸네일 URL)
    running_time: str  # Running Time (재생 시간)
    is_available: bool  # Available in Laftel (라프텔 시청 가능 여부)
    assetid: str  # Asset ID (에셋 아이디)

    def __init__(self, data):
        self.id = data.get("id")
        self.title = data.get("title")
        self.subject = data.get("subject")
        self.description = data.get("description")
        self.episode_num = data.get("episode_num")
        self.episode_order = data.get("episode_order")
        self.thumbnail_path = data.get("thumbnail_path")
        self.running_time = data.get("running_time")
        self.is_available = data.get("is_available")
        self.assetid = "/".join(self.thumbnail_path.split("/")[4:7])
