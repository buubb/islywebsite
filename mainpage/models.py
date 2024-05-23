from django.db import models

class special_activities_tab(models.Model):
    subtitle = models.CharField("태그(#)",max_length=50,default="tag")
    title = models.CharField("제목",max_length =100)
    content = models.TextField("내용",max_length=250)
    category = models.IntegerField("그림", choices=[(0, 'Get The Flag'), (1, 'networking'), (2, 'Education')], default=1)

    class Meta:
        verbose_name = '특별활동 리스트'
        verbose_name_plural = 'Special Activities'

    def __str__(self):
        return self.title
    
class activity_records_count(models.Model):
    years = models.IntegerField("운영 기간")
    applicants = models.IntegerField("지원자 수")
    members = models.IntegerField("활동 부원 수")
    projects = models.IntegerField("누적 프로젝트 수")

    class Meta:
        verbose_name = '동아리 활동 기록'
        verbose_name_plural = 'Activity Record'

class InstagramToken(models.Model):
    token = models.TextField("instagram_token")
    last_updated = models.DateTimeField("최종수정일",auto_now=True)

    def __str__(self):
        return self.token