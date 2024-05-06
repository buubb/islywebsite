from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField("프로필 이미지", upload_to="users/profile", blank=True)
    short_description = models.TextField("소개글", blank=True)
    like_posts = models.ManyToManyField(
        "volunteer.Post",
        verbose_name="좋아요 누른 Post 목록",
        related_name="like_users",
        blank=True,
    )

    def __str__(self):
        return self.username
