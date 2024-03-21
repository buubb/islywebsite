from django.db import models

class special_activities_tab(models.Model):
    title = models.CharField("제목",max_length =100)
    content = models.TextField("내용",max_length=250)
    image = models.ImageField("사진",upload_to="images",null=True)

    class Meta:
        verbose_name = '특별활동 리스트'
        verbose_name_plural = 'Special Activities'

    def __str__(self):
        return self.title
    
class activity_records_count(models.Model):
    years = models.IntegerField("누적 년도")
    applicants = models.IntegerField("누적 지원자 수")
    members = models.IntegerField("누적 부원 수")
    projects = models.IntegerField("누적 프로젝트 수")

    class Meta:
        verbose_name = '동아리 누적 활동 기록'
        verbose_name_plural = 'Activity Record'
