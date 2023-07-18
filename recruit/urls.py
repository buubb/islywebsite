from django.urls import path
from .views import Recruit

urlpatterns = [
    # url path: recruit/
    path('', Recruit.as_view())
]