# -*- conding: utf-8 -*-
import laftel

query = input("검색할 애니 이름을 입력하세요: ")

data = laftel.sync.searchAnime(query)  # List[SearchResult]
print(data[2])
for results in data:
    print(f"{data.index(results)}. {results.name}")

data = laftel.sync.getAnimeInfo(data[int(input("번호를 입력하세요: "))].id)  # AnimeInfo

print(data)

"""
Example SearchResult:

SearchResult(
id=40163, 
name='전생했더니 슬라임이었던 건에 대하여 2기', 
url='https://laftel.net/item/40163', 
image='https://image.laftel.net/items/thumbs/big/76bca22c-b55f-4f9d-aecd-6e4061d2a15a.jpg', 
adultonly=False, 
genres=['판타지', '액션', '개그', '모험'], 
get_data=<function searchAnime.<locals>.get_data at 0x000001FFF94A29D0>
)
"""

"""
Example AnimeInfo: 

AnimeInfo(
id=40163,
name='전생했더니 슬라임이었던 건에 대하여 2기',
url='https://laftel.net/item/40163',
image='https://image.laftel.net/items/thumbs/big/76bca22c-b55f-4f9d-aecd-6e4061d2a15a.jpg',
content="주인공 리무루와 그를 따르는 다수의 마물들이 세운 나라 '쥬라 템페스트 연방국'은 근린 국가들과의 협정과 교역을 통해 '인간과 마물이 공존하는 나라'라는 이상을 현실로 만들려 하고 있었다. 이는 인간이었던 슬라임에서 기인한 리무루의 '인간에 대한 호의'였다...... 하지만 이 세계에는 명확한 '마물에 대한 적의'가 존재하고 있었다. 그 불합리한 현실을 마주했을 때, 리무루는 선택한다.\n'무엇을 잃고 싶지 않은지'를───",
ended=True,
awards=['라프텔 역대 애니 인기 랭킹 89위'],
content_rating='15세 이용가',
adultonly=False,
viewable=True, 
genres=['판타지', '액션', '개그', '모험'], 
tags=['마법', '이세계', '요괴 및 괴물', '전쟁', '이능력', '악마 또는 천사', '마왕', '환생', '발랄가볍', '먼치킨', '판타지', '액션', '개그', '모험', '상상의 장소'], 
air_year_quarter='2021년 1분기', 
air_day='목요일', 
avg_rating=4.5868482920757, 
view_male=1604, 
view_female=449
)
"""
