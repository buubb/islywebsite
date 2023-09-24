from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(title), 내용(content)이 존재합니다.

class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
#복사본
