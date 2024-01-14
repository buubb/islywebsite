from django.urls import path
from .views import BasicList, BasicPosting, AdvancedList, AdvancedPosting, BasicCreate, AdvancedCreate

urlpatterns = [
    # url path: assignments/advanced/
    path('advanced/', AdvancedList, name='advanced'),
    # url path : assignments/basic/
    path('basic/', BasicList, name='basic'),

    # URL:80/assignments/basic/숫자로 접속하면 게시글-세부페이지(posting)
    path('basic/<int:post_id>/', BasicPosting, name="BasicPosting"),
    # URL:80/assignments/advanced/숫자로 접속하면 게시글-세부페이지(posting)
    path('advanced/<int:post_id>/', AdvancedPosting, name="AdvancedPosting"),

    # BasicCreate 뷰에 대한 URL 패턴을 추가합니다.
    path('basic/create/', BasicCreate, name='basic_create'),
    # AdvancedCreate 뷰에 대한 URL 패턴을 추가합니다.
    path('advanced/create/', AdvancedCreate, name='advanced_create'),

]