from django.urls import path
from .views import TeamActivities, TeamWritePage, TeamActivitiesView


urlpatterns = [
    # 링크의 주소 대신 별칭을 사용하려면 name 변수 사용
    # url path: team-activities/
    path('', TeamActivitiesView.as_view(), name='team_list'),
    path('web/', TeamActivities.as_view()),
    path('rev/', TeamActivities.as_view()),
    path('pwn/', TeamActivities.as_view()),
    path('adv/', TeamActivities.as_view()),
    path('write/', TeamWritePage.as_view()),
    
]