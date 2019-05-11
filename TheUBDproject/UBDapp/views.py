from django.shortcuts import render
import datetime
from bs4 import BeautifulSoup
import requests
# Create your views here.


def home(request):

    # time on now
    time_now = datetime.datetime.now()

    return render(request, 'index.html', {'now': time_now})


def ubdresult(request):

    # for crawling
    req = requests.get(
        'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%97%84%EB%B3%B5%EB%8F%99+%EA%B4%80%EA%B0%9D%EC%88%98')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find("div", class_="movie_info section").find("div", class_="info_main").find(
        "dl", class_="desc_detail").find("span", class_="property").text
    noa = info.replace("명", "", 1).replace(",", "", 1)

    ubd_int = float(request.GET['ubdint']) / int(noa)
    ubd_rep = round(ubd_int, 3)

    return render(request, 'ubdresult.html', {'ubdrep': ubd_rep})

def ubdresult_rev(request):

    # for crawling
    req = requests.get(
        'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%97%84%EB%B3%B5%EB%8F%99+%EA%B4%80%EA%B0%9D%EC%88%98')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find("div", class_="movie_info section").find("div", class_="info_main").find(
        "dl", class_="desc_detail").find("span", class_="property").text
    noa = info.replace("명", "", 1).replace(",", "", 1)

    ubd_rev = float(request.GET['ubdint_rev']) * int(noa)
    ubd_revrep = round(ubd_rev, 3)

    return render(request, 'ubdresult_rev.html', {'ubdrev' : ubd_revrep})   
