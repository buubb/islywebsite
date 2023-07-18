from django.urls import path
from .views import Introduction

urlpatterns = [
    # url path: introduction/
    path('', Introduction.as_view()),
]