from django.urls import path
from .views import recruit


app_name = "Recruit"
urlpatterns = [
    # url path: recruit/
    path("", recruit, name="recruit"),
]