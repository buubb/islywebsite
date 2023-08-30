from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from User.models import User

#admin.site.register(User, UserAdmin) #user는 내가 만든거, useradmin은 장고제공사용

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ("username", "password"),
            },
        ),
        ("개인정보", {"fields": ("first_name", "last_name", "email")}),
        (
            "추가필드",
            {
                "fields": ("profile_image", "short_description"),
            },
        ),
        (
            "권한",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "중요한 일정",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    ]