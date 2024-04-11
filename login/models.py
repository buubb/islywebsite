from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

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
    
from django.contrib.auth.signals import user_logged_in
from django.db import models

from importlib import import_module


SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    session_key = models.CharField(max_length=40, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def kicked_my_other_sessions(sender, request, user, **kwargs):
        for user_session in UserSession.objects.filter(user=user):
            session_key = user_session.session_key
            session = SessionStore(session_key)
            # session.delete()
            session['kicked'] = True
            session.save()
            user_session.delete()

        session_key = request.session.session_key
        UserSession.objects.create(user=user, session_key=session_key)

    user_logged_in.connect(kicked_my_other_sessions, dispatch_uid='user_logged_in')