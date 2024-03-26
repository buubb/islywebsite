from django.urls import path
from .views import recruit, check_status


app_name = "Recruit"
urlpatterns = [
    # url path: recruit/
    path("", recruit, name="recruit"),
    path("result/", check_status, name="check_status"),
]