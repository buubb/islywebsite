from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class LoginFail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.timestamp}'