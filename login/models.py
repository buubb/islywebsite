# models.py

from django.db import models

class LoginAttempt(models.Model):
    ip = models.CharField(max_length=50)
    attempt = models.PositiveIntegerField(default=0)
    lock = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)