from django.urls import path
from .views import CTFChallenge

urlpatterns = [
    path('', CTFChallenge.as_view()),
]