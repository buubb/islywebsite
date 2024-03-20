from django.contrib import admin
from main.models import SpecialActivitiesPost, ActivityRecordsCount
class SpecialActivitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','img')
class ActivityRecordsCountAdmin(admin.ModelAdmin):
    list_display = ('years','applicants','members','projects')
    
admin.site.register(SpecialActivitiesPost)
admin.site.register(ActivityRecordsCount)