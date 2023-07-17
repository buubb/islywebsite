from django.urls import path
from .views import Introduction

urlpatterns = [
    path('', Introduction.as_view()),
]