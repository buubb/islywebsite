from django.urls import path
from .views import AssignmentsList, AssignmentsSubmit

urlpatterns = [
    path('list/', AssignmentsList.as_view()),
    path('submit/', AssignmentsSubmit.as_view())
]