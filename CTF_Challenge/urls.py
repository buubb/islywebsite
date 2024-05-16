# urls.py
from django.urls import path
from .views import wargame, add_player, edit_player, snake, flag


app_name = "CTFChallenge"
urlpatterns = [
    # url path: wargame/
    path("", wargame, name="wargame"),
    path("add_player/", add_player, name="add_player"),
    path("edit_player/<int:player_id>/", edit_player, name="edit_player"),
    path("snake/", snake, name="snake"),
    path("flag/", flag, name="flag"),
]
