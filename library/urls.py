from django.urls import path
from .views import Library

urlpatterns = [
    path('', Library.as_view()),
]