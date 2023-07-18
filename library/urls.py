from django.urls import path
from .views import Library

urlpatterns = [
    # url path: library/
    path('', Library.as_view()),
]