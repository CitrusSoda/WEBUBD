# parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    '#boxoffice > div.rolling_content > ul'
    )
# my_titles는 list 객체
for title in my_titles:
    # Tag안의 텍스트
    print(title.text)
    # Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))