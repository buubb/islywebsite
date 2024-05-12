# admin.py

from django.contrib import admin
from .models import LoginAttempt

@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ['ip', 'attempt', 'lock', 'timestamp']
    ordering=['timestamp']
