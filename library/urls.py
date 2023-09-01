from django.urls import path
from .views import Library, Library_Write

urlpatterns = [
    # url path: library/
    path('', Library.as_view()),
    path('write/', Library_Write.as_view())
]

