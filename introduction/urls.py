from django.urls import path
from .views import introduction, bylaws, developers


app_name = "Introduction"
urlpatterns = [
    # url path: introduction/
    path("", introduction, name="introduction"),
    path("bylaws/", bylaws, name="bylaws"),
    path("developers/", developers, name="developers"),
]
