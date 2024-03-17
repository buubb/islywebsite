# admin.py
from django.contrib import admin
from .models import Recruitment, Announcement


admin.site.register(Recruitment)
admin.site.register(Announcement)