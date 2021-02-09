class AnimeInfo:
    def __init__(self, data):
        self.rawdata = data

        self.id = int()  #ID
        self.name = str()  #작품 이름
        self.image = str()  #작품 커버 사진
        self.content = str()  #간단 줄거리
        self.ended = bool()  #완결 여부
        self.awards = list()  #받은 상 리스트 (문자열)

        self.content_rating = str() #영상물 등금 (15세 이용가)
        self.adultonly = bool()  #성인인증 필요유무
        self.viewable = bool()  #라프텔 시청 가능 여부
        self.genres = list()  #장르들 list로
        self.tags = list()  #라프텔에서 붙인 태그 확인용
        

        self.air_year_quarter = str()  #방영 분기 (2021년도 1분기)
        self.air_time = str()  #연재 요일 (일요일)
        self.avg_rating = float()  #평균별점

        self.view_male = int()  #남성 시청 비율
        self.view_female = int()  #여성 시청 비율
