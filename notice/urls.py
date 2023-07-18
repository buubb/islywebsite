from django.urls import path
from .views import Notice

urlpatterns = [
    # url path: notice/
    path('', Notice.as_view())
]