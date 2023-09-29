from django.urls import path

from . import views

urlpatterns = [
    # url path: library/
    path('', views.Library, name='Library'),
    path('<int:post_id>/', views.posting, name='posting'),
    path('create/', views.post_create, name='post_create'),
]
