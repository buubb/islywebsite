from django.urls import path
from .views import Login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url path: login/
    path('', Login.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login/make.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]