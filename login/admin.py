# admin.py

from django.contrib import admin
from .models import LoginAttempt

@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'username', 'success', 'timestamp']
    list_filter = ['success', 'timestamp']
    search_fields = ['ip_address', 'username']
