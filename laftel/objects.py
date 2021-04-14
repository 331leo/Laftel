from dataclasses import dataclass

@dataclass(repr=True)
class AnimeInfo:
    id: int #ID
    name: str #작품 이름
    image: str #작품 커버 사진
    content: str #간단 줄거리
    ended: bool #완결 여부
    awards: list #받은 상 리스트 (문자열)

    content_rating: str #영상물 등금 (15세 이용가)
    adultonly: bool #성인애니 유무
    viewable: bool #라프텔 시청 가능 여부
    genres: list #장르들 list로
    tags: list #라프텔에서 붙인 태그 확인용

    air_year_quarter: str #방영 분기 (2021년도 1분기)
    air_time: str #연재 요일 (일요일)
    avg_rating: float #평균별점
 
    view_male: int #남성 시청 비율
    view_female: int #여성 시청 비율

    def __init__(self, data):
        self.rawdata = data

@dataclass(repr=True)
class SearchResult:
    id: int  #ID
    name: str  #작품 이름
    image: str  #작품 커버 사진
    adultonly: bool  #성인애니 유무
    genres: list  #장르들 list로
    
    get_data: object #AnimeInfo를 리턴받을 수 있는 함수

    def __init__(self, data):
        self.rawdata = data