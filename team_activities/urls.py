from django.urls import path
from .views import TeamActivities

urlpatterns = [
    # url path: team-activities/
    path('', TeamActivities.as_view()),
]