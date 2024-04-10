# admin.py
from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name", "point", "challenge", "profile_image", "dreamhack_link"]
    # readonly_fields = ["ranking"]
