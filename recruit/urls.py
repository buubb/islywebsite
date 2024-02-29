from django.urls import path
from .views import recruit, status


app_name = "Recruit"
urlpatterns = [
    # url path: recruit/
    path("", recruit, name="recruit"),
    path("status/", status, name="status"),
]