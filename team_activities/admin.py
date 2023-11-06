from django.contrib import admin
from .models import TeamActivitiesPost
# Register your models here.

class TeamActivitiesAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'author',
        'hits',
        'registered_date',
    )
    search_fields=('title', 'content','author',)

admin.site.register(TeamActivitiesPost, TeamActivitiesAdmin)