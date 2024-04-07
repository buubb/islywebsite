# urls.py
from django.urls import path
from .views import notice


urlpatterns = [
    # url path: notice/
    path('', notice, name="notice")
]
