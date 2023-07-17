from django.urls import path
from .views import Notice

urlpatterns = [
    path('', Notice.as_view())
]