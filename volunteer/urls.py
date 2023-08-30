from django.urls import path
from .views import Volunteer

urlpatterns = [
    # url path: volunteer/
    path('', Volunteer.as_view()),
]
