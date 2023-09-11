from django.urls import path
from .views import ( Volunteer, post_like, )

app_name = "Volunteer"
urlpatterns = [
    # url path: volunteer/
    path('', Volunteer.as_view(), name="volunteer"),
    path("<int:post_id>/like/", post_like, name="post_like"),
]
