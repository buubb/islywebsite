from django.urls import path
from .views import TeamActivities

urlpatterns = [
    path('', TeamActivities.as_view()),
]