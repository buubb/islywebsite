from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import TeamWebPosting, TeamRevPosting, TeamPwnPosting, TeamAdvPosting, TeamWritePage, TeamActivitiesView


urlpatterns = [
    # 링크의 주소 대신 별칭을 사용하려면 name 변수 사용
    # url path: team-activities/
    path('', TeamActivitiesView.as_view(), name='team_list'),
    # url path: team-activities/web/숫자로 접속하면 게시글-세부페이지
    path('web/<int:post_id>/',TeamWebPosting, name="TeamWebPosting"),
    path('rev/<int:post_id>/',TeamRevPosting, name="TeamRevPosting"),
    path('pwn/<int:post_id>/',TeamPwnPosting, name="TeamPwnPosting"),
    path('adv/<int:post_id>/',TeamAdvPosting, name="TeamAdvPosting"),
    #TeamWritePage 뷰에 대한 URL 패턴 추가
    path('write/', TeamWritePage.as_view(), name="TeamWritePage"),
    
]