"""TheUBD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import UBDapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UBDapp.views.home, name='home'),
    path("result/", UBDapp.views.ubdresult, name='ubdresult'),
    path('resultrev/', UBDapp.views.ubdresult_rev, name='ubdresult_rev'),
    path(r'base_layout', UBDapp.views.home, name='base_layout'),
    path('', include('pwa.urls')),
]
