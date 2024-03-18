from django.urls import path
from main.views import Main

urlpatterns = [
    # url path: /
    path('', Main.as_view()),
    
]