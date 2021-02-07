class AnimeInfo:
    def __init__(self, data):
        self.id = int()  #ID
        self.name = str()  #작품 이름
        self.image = str()  #작품 커버 사진
        self.content = str()  #간단 줄거리
        self.ended = bool()  #완결 여부

        self.air_year_quarter = str()  #2021년도 1분기 
        self.distributed_air_time = str()  #일요일

        self.viewable = bool()  #라프텔 시청 가능 여부
        self.genres = list()  #장르들 list로
        self.adultonly = bool()  #성인인증 필요유무
        self.tags = list()  #라프텔에서 붙인 태그 확인용
        self.rating = float()  #평균별점
        self.rawdata = data
