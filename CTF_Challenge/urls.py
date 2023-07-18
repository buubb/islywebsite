from django.urls import path
from .views import CTFChallenge

urlpatterns = [
    # url path: CTF-Challenge/
    path('', CTFChallenge.as_view()),
]