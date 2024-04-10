# urls.py
from django.urls import path
from .views import ctf


app_name = "CTFChallenge"
urlpatterns = [
    # url path: CTF-Challenge/
    path("", ctf, name="ctf"),
]