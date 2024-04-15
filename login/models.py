from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from importlib import import_module

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

from django.contrib.auth.models import AbstractUser, Group, Permission

#계정 잠금 관련 코드
class CustomUser(AbstractUser):
    is_locked = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    def lock_account(self):
        self.is_locked = True
        self.save()

    def unlock_account(self):
        self.is_locked = False
        self.save()

class LoginFail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='login_fails')
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.timestamp}'

    
# ---------------------------------------------------------

# class UserSession(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
#     session_key = models.CharField(max_length=40, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def kicked_my_other_sessions(sender, request, user, **kwargs):
#         for user_session in UserSession.objects.filter(user=user):
#             session_key = user_session.session_key
#             session = SessionStore(session_key)
#             # session.delete()
#             session['kicked'] = True
#             session.save()
#             user_session.delete()

#         session_key = request.session.session_key
#         UserSession.objects.create(user=user, session_key=session_key)

#     user_logged_in.connect(kicked_my_other_sessions, dispatch_uid='user_logged_in')