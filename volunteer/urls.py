from django.urls import path
from .views import Volunteer

urlpatterns = [
    path('', Volunteer.as_view()),
]