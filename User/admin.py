from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from User.models import User

admin.site.register(User, UserAdmin) #user는 내가 만든거, useradmin은 장고제공사용