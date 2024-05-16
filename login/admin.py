from django.contrib import admin
from .models import LoginFails

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['login_attempts', 'locked', 'ip_address', 'login_time']
    readonly_fields = ['ip_address', 'login_time']
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
    delete_selected.short_description = "Delete selected User Login Fails records"

admin.site.register(LoginFails, UserProfileAdmin)