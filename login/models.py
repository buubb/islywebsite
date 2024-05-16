from django.db import models

class LoginFails(models.Model):
    login_attempts = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)
    ip_address = models.CharField(max_length=100, default='')  # 로그인 시도한 IP 주소
    login_time = models.DateTimeField(auto_now_add=True)  # 로그인 시도 시간