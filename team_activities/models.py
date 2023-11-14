import os
from django.db import models
from django.conf import settings
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
# Create your models here.

class TeamActivitiesPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    content=MarkdownxField(verbose_name='내용')
    hits=models.PositiveIntegerField(verbose_name='조회수',default=0)
    registered_date=models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    top_fixed=models.BooleanField(verbose_name='상단고정', default=False)

    def __str__(self):
        return self.title
    
    def get_content_markdown(self):
        return markdown(self.content)
    
    class Meta:
        db_table = 'teampost'
        verbose_name='teampost'
        verbose_name_plural='teampost'