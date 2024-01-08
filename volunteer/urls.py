from django.urls import path
from .views import feed, post_detail, post_like, load_more

app_name = "Volunteer"
urlpatterns = [
    # url path: volunteer/
    path("", feed, name="feed"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    path("<int:post_id>/like/", post_like, name="post_like"),
    path("load_more/", load_more, name="load_more"),
]
