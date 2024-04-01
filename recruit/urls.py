# urls.py
from django.urls import path
from .views import recruit, check_phone_number, check_student_id, pass_page, fail_page

app_name = "Recruit"
urlpatterns = [
    # url path: recruit/
    path("", recruit, name="recruit"),
    path("check_phone_number/", check_phone_number, name="check_phone_number"),
    path("check_student_id/", check_student_id, name="check_student_id"),
    path("pass/", pass_page, name="pass"),
    path("fail/", fail_page, name="fail"),
]