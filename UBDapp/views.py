from django.shortcuts import render, redirect
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

    # for crawling
    req = requests.get(
        'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles_soup = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.movie_info > dl > dd:nth-child(2)'
    )

    for i in range(len(my_titles_soup)):
        my_titles_soup[i] = my_titles_soup[i].text

    my_titles2_soup = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div > a > div > strong'
    )

    for i in range(len(my_titles2_soup)):
        my_titles2_soup[i] = my_titles2_soup[i].text

    my_titlesday_soup = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.movie_info > dl > dd:nth-child(4)'
    )
    my_titlesday = []
    for i in range(len(my_titlesday_soup)):
        my_titlesday.append(round(float(my_titlesday_soup[i].text.replace(
            "명", "").replace(",", "")) / int(noa), 2))

    my_titlesall_soup = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.movie_info > dl > dd:nth-child(6)'
    )
    my_titlesall = []
    for i in range(len(my_titlesall_soup)):
        my_titlesall.append(round(float(my_titlesall_soup[i].text.replace(
            "명", "").replace(",", "")) / int(noa), 2))

    my_image = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.thumb > a > img'
    )

    my_link = soup.select(
        '#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel.v2 > div:nth-child(1) > ul > li > div.thumb > a'
    )

    movies = []
    for i in range(len(my_image)):
        movies.append({'movie_title': my_titles2_soup[i], 'infor': my_titles_soup[i], 'day_ubd': "일간 UBD : " + str(my_titlesday[i]), 'total_ubd': " 누적 UBD : " + str(my_titlesall[i]),
                       'image': my_image[i].get("src"), 'link': my_link[i].get("href")})
    # return render(request, 'index.html', {'now': time_now, 'my_titles_res': my_titles_result, 'my_image': my_image})
    return render(request, 'index.html', {'now': time_now, 'movies': movies})


def ubdresult(request):
    if request.GET['ubdint'] == "":
        return redirect('home')

    ubd_int = float(request.GET['ubdint']) / int(noa)
    ubd_rep = round(ubd_int, 3)

    return render(request, 'ubdresult.html', {'ubdrep': ubd_rep, 'now': time_now})


def ubdresult_rev(request):
    if request.GET['ubdint_rev'] == "":
        return redirect('home')

    ubd_rev = float(request.GET['ubdint_rev']) * int(noa)
    ubd_revrep = round(ubd_rev, 3)

    return render(request, 'ubdresult_rev.html', {'ubdrev': ubd_revrep, 'now': time_now})


def base_layout(request):
    template = 'base.html'
    return render(request, template)
