# urls.py
from django.urls import path
from .views import (
    feed,
    load_more,
    post_add,
    post_detail,
    post_edit,
    post_delete,
    post_like,
    comment_add,
    comment_delete,
)

app_name = "Volunteer"
urlpatterns = [
    # url path: project/
    path("", feed, name="feed"),
    path("load_more/", load_more, name="load_more"),
    path("post_add/", post_add, name="post_add"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    path("<int:post_id>/edit/", post_edit, name="post_edit"),
    path("<int:post_id>/delete/", post_delete, name="post_delete"),
    path("<int:post_id>/like/", post_like, name="post_like"),
    path("<int:post_id>/comment_add/", comment_add, name="comment_add"),
    path("comment_delete/<int:comment_id>/", comment_delete, name="comment_delete"),
]
