from django.urls import path
# from .views import Introduction
from .views import introduction, rules

app_name = "Introduction"
urlpatterns = [
    # url path: introduction/
    # path('', Introduction.as_view()),
    path("", introduction, name="introduction"),
    path("rules/", rules, name="rules"),
]