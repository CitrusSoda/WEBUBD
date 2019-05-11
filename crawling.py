# parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.movie_info > dl > dd:nth-child(4)'
    )

my_titles2 = soup.select(
    '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div > a > div > strong'
)

# my_titles는 list 객체
for title in my_titles:
    # Tag안의 텍스트
    a = title.text
    print(a)
    
for title2 in my_titles2:
    b = title2.text
    print(b)
