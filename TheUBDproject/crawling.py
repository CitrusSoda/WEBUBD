import requests
from bs4 import BeautifulSoup


req = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%97%84%EB%B3%B5%EB%8F%99+%EA%B4%80%EA%B0%9D%EC%88%98')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
info = soup.find("div", class_="movie_info section").find("div", class_="info_main").find("dl", class_="desc_detail").find("span", class_="property").text
noa = info.replace("명", "",1).replace(",", "",1)


print(int(noa))
