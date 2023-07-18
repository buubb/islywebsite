from django.urls import path
from .views import Login

urlpatterns = [
    # url path: login/
    path('', Login.as_view()),
]