from django.urls import path
from .views import BasicBlog, BasicPosting, AdvancedBlog, AdvancedPosting

urlpatterns = [
    # url path: assignments/advanced/
    path('advanced/', AdvancedBlog),
    # url path : assignments/basic/
    path('basic/', BasicBlog),
    # url path : assignments/submit/
    path('submit/', BasicBlog),

    # URL:80/assignments/basic/숫자로 접속하면 게시글-세부페이지(posting)
    path('basic/<int:post_id>/', BasicPosting, name="BasicPosting"),

    # URL:80/assignments/advanced/숫자로 접속하면 게시글-세부페이지(posting)
    path('advanced/<int:post_id>/', AdvancedPosting, name="AdvancedPosting"),
]