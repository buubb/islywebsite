from django.urls import path

from . import views

urlpatterns = [
    # url path: library/
    path('', views.Library, name='Library'),
    path('<int:post_id>/', views.posting, name='posting'),
    path('create/', views.post_create, name='post_create'),
    path('modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/create/library/<int:post_id>/', views.comment_create_library, name='comment_create_library'),
    path('comment/modify/library/<int:comment_id>/', views.comment_modify_library, name='comment_modify_library'),
    path('comment/delete/library/<int:comment_id>/', views.comment_delete_library, name='comment_delete_library'),
]
