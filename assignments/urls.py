from django.urls import path
from .views import AdvancedList, Submit, BasicList

urlpatterns = [
    # url path: assignments/advanced/
    path('advanced/', AdvancedList.as_view()),
    # url path : assignments/basic/
    path('basic/', BasicList.as_view()),
    # url path : assignments/submit/
    path('submit/', Submit.as_view()),
]