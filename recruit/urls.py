from django.urls import path
from .views import Recruit

urlpatterns = [
    path('', Recruit.as_view())
]