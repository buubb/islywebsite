from django.db import models


class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=50, null=True)
    year = models.PositiveIntegerField("연도", null=True)
    generation = models.PositiveIntegerField("동아리 기수", null=True)
    user = models.ForeignKey("User.User", verbose_name="작성자", on_delete=models.CASCADE)
    content = models.TextField("내용", blank=True)
    created = models.DateTimeField("작성일시", auto_now=True, null=True)

    def __str__(self):
        return f"{self.user.username}의 Post(id: {self.id})"


class PostImage(models.Model):
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    photo = models.ImageField("사진", upload_to="post")


class Comment(models.Model):
    user = models.ForeignKey("User.User", verbose_name="작성자", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    name = models.CharField("이름", max_length=10, null=True)
    content = models.TextField("내용")
    created = models.DateTimeField("작성일시", auto_now=True)
