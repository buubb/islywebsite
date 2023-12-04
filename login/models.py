from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class LoginFail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    
    # 다음 두 줄은 필수는 아니지만 추가적인 정보로 사용할 수 있습니다.
    # 예를 들어, 언제 사용자가 잠금을 풀었는지 기록할 수 있습니다.

    def __str__(self):
        return f'{self.user.username} - {self.timestamp}'