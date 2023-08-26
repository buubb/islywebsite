from django.db import models

# Create your models here.

class Library(models.Model):
    title = models.CharField(max_length=64, verbose_name= '글 제목')
    contents = models.TextField(verbose_name='글 내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    writer_dttm = models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')
    
    updata_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')
    

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'library'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'