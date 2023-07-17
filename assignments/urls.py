from django.urls import path
from .views import AdvancedList, Submit, BasicList

urlpatterns = [
    path('advanced/', AdvancedList.as_view()),
    path('basic/', BasicList.as_view()),
    path('submit/', Submit.as_view())
]