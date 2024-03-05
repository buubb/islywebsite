from django.urls import path
from .views import Login
from django.contrib.auth import views as auth_views
from .views import check_session_status

from . import views

""" urlpatterns=[
    path('', Login.as_view(), name='login'),  # /login/ 에 대한 로그인 뷰
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] """

urlpatterns = [
    # url path: login/
    path('', Login.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login/new2.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('check_session_status/', check_session_status, name='check_session_status'),
   ]
