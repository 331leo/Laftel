<h3 align="center"> <img src="https://asset.laftel.net/static/media/purple.e17b0b50.svg" alt="img" width="30" height=""> Laftel <img src="https://asset.laftel.net/static/media/purple.e17b0b50.svg" alt="img" width="30" height=""> </h3>

<h6 align="center">Unofficial Python Laftel.net API Wrapper</h6>

<div align="center" id="badges"> <img src="https://img.shields.io/pypi/pyversions/laftel?color=816BFF&style=flat-square"> <img src="https://img.shields.io/pypi/v/laftel?color=816BFF&label=laftel&logo=python&logoColor=816BFF&style=flat-square"> <img src="https://img.shields.io/pypi/l/laftel?color=816BFF&logo=gnu&logoColor=816BFF&style=flat-square"> <img src="https://img.shields.io/pypi/dm/laftel?color=816BFF&style=flat-square"> <img src="https://img.shields.io/pypi/status/laftel?color=816BFF&style=flat-square">  </div>

---

## Installation

Requires Python 3.6 or upper

```bash
python3 -m pip install laftel
```

## Usage

```python
import laftel

# Synchronous
def main():
    laftel.sync.searchAnime("전생슬") # -> List[SearchResult]
    laftel.sync.getAnimeInfo(SerachResult.id) # -> AnimeInfo

# Asynchronous
async def main():
    await laftel.searchAnime("전생슬") # -> List[SearchResult]
    await laftel.getAnimeInfo(SerachResult.id) # -> AnimeInfo
```

## Models

```python
SearchResult:

    id: int # Anime ID (애니 아이디)
    name: str # Anime Title (애니 제목)
    url: str # Anime Link (애니 링크)
    image: str # Cover image URL (커버 사진 URL)
    adultonly: bool # Adult Content (성인인증 필요 여부)
    genres: List[str] # Genres in korean string (장르 태그 목록)

    get_data: Callable # Function returns AnimeInfo for this anime (AnimeInfo 가져오는 함수)

```

```python
AnimeInfo:

    id: int # Anime ID (애니 아이디)
    name: str # Anime Title (애니 제목)
    url: str # Anime Link (애니 링크)
    image: str # Cover image URL (커버 사진 URL)
    content: str  # Summary of anime (애니 줄거리)
    ended: bool # Anime complete or not (애니 완결 여부)
    awards: List[str]  # Arards that granted to anime (애니가 받은 상 목록)

    content_rating: str  # Content Rating in korean (콘텐츠 등급 - 00세 이용가)
    adultonly: bool # Adult Content (성인인증 필요 여부)
    viewable: bool  # Available in Laftel (라프텔 시청 가능 여부)
    genres: List[str] # Genres in korean string (장르 태그 목록)
    tags: List[str]  # Anime tags from Laftel (라프텔이 붙인 태그)

    air_year_quarter: str  # Airing quarter (방영분기 - 2020년 1분기)
    air_day: str  # Airing day (방영 요일)
    avg_rating: float  # Average User Rating out of 5 (5점 만점 중 평균 별점)

    view_male: int  # Percentage of male in total watched user (남성 시청자 비율)
    view_female: int  # Percentage of woman in total watched user (남성 시청자 비율)
```

## Example

[View example.py](example.py)
