from django.urls import path
from .views import TeamActivities, TeamWritePage


urlpatterns = [
    # 링크의 주소 대신 별칭을 사용하려면 name 변수 사용
    # url path: team-activities/
    path('', TeamActivities.as_view()),
    path('web/', TeamActivities.as_view()),
    path('rev/', TeamActivities.as_view()),
    path('pwn/', TeamActivities.as_view()),
    path('adv/', TeamActivities.as_view()),
    path('write/', TeamWritePage.as_view()),
    
]