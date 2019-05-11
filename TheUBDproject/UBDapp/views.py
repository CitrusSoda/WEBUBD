from django.shortcuts import render
import datetime
from bs4 import BeautifulSoup
import requests
# Create your views here.

# time on now
time_now = datetime.datetime.now()

# for crawling
req = requests.get(
    'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%97%84%EB%B3%B5%EB%8F%99+%EA%B4%80%EA%B0%9D%EC%88%98')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
info = soup.find("div", class_="movie_info section").find("div", class_="info_main").find(
    "dl", class_="desc_detail").find("span", class_="property").text
noa = info.replace("명", "", 1).replace(",", "", 1)


def forPrint(array):
    for item in array:
        return item.text

def home(request):

    #for crawling
    req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles_soup = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.movie_info > dl > dd:nth-child(2)'
    )

    my_titles = []
    for item1 in my_titles_soup:
        my_titles.append(item1.text)

    for i in range(len(my_titles_soup)):
        my_titles_soup[i] = my_titles_soup[i].text


    my_titles2_soup = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div > a > div > strong'
    )

    my_titles_2 = []
    for item2 in my_titles2_soup:
        my_titles_2.append(item2.text)

    for i in range(len(my_titles2_soup)):
        my_titles2_soup[i] = my_titles2_soup[i].text

    my_titlesday_soup = soup.select(
    '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.movie_info > dl > dd:nth-child(4)'
    )

    my_titles_day = []
    for item3 in my_titlesday_soup:
        for_ubd_day = item3.text.replace("명","").replace(",","")
        my_titles_day.append(for_ubd_day)

    for i in range(len(my_titlesday_soup)):
        my_titlesday_soup[i] = my_titlesday_soup[i].text    

    my_titles_result = []
    for i in range(len(my_titles2_soup)):
        my_titles_result.append(my_titles2_soup[i] + my_titles_soup[i] + my_titlesday_soup[i])

    return render(request, 'index.html', {'now': time_now, 'my_titles_res': my_titles_result})

def ubdresult(request):


    ubd_int = float(request.GET['ubdint']) / int(noa)
    ubd_rep = round(ubd_int, 3)

    return render(request, 'ubdresult.html', {'ubdrep': ubd_rep, 'now': time_now})


def ubdresult_rev(request):


    ubd_rev = float(request.GET['ubdint_rev']) * int(noa)
    ubd_revrep = round(ubd_rev, 3)

    return render(request, 'ubdresult_rev.html', {'ubdrev': ubd_revrep, 'now': time_now})


def base_layout(request):
	template='base.html'
	return render(request,template)