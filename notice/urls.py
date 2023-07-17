from django.urls import path
from .views import Notice

urlpatterns = [
    path('notice/', Notice.as_view())
]