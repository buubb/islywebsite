from django.contrib import admin
from .models import LoginFail, CustomUser

# admin페이지에서 잠금 해제할 수 있는 기능
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_locked']
    actions = ['unlock_accounts']

    def lock_accounts(self, request, queryset):
        queryset.update(is_locked=True)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(LoginFail)