# urls.py
from django.urls import path
from .views import wargame


app_name = "CTFChallenge"
urlpatterns = [
    # url path: CTF-Challenge/
    path("", wargame, name="wargame"),
]