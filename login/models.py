# models.py

from django.db import models

class LoginAttempt(models.Model):
    ip_address = models.CharField(max_length=50)
    username = models.CharField(max_length=100, null=True, blank=True)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
