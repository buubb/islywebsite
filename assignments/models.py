from django.db import models
from django.conf import settings
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# author은 settings 의 User 테이블 사용

class BasicAssignment(models.Model): # models 모듈의 Model 클래스를 확장하여 만든 클래스
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = MarkdownxField()
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True, default='default_value.pdf')
    created_at = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def get_content_markdown(self):  # 추가
        return markdown(self.content)

class AdvancedAssignment(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = MarkdownxField()
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True, default='default_value.pdf')
    created_at = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def get_content_markdown(self):  # 추가
        return markdown(self.content)