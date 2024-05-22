from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    short_description = models.TextField("소개글", blank=True)
    like_posts = models.ManyToManyField(
        "volunteer.Post",
        verbose_name="좋아요 누른 Post 목록",
        related_name="like_users",
        blank=True,
    )

    def __str__(self):
        return self.username
