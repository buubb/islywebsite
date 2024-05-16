from django.urls import path
from .views import Login, CheckLogin
from django.contrib.auth import views as auth_views
from .views import blocked_view

from . import views

""" urlpatterns=[
    path('', Login.as_view(), name='login'),  # /login/ 에 대한 로그인 뷰
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] """

urlpatterns = [
    # url path: login/
    path('', Login.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login/new3.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('check/', CheckLogin.as_view(), name='check'),
    path('change_password/', views.password_edit_view, name='change_password'),
    path('blocked/', blocked_view, name='blocked'),
   ]