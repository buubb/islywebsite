# models.py
from django.db import models
from django.utils import timezone


class Player(models.Model):
    user = models.ForeignKey("User.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    point = models.IntegerField()
    challenge = models.IntegerField()
    profile_image = models.ImageField(upload_to="ctf/profile")
    dreamhack_link = models.URLField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.updated is None:
            self.updated = timezone.now()
        super().save(*args, **kwargs)