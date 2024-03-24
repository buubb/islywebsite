from django.contrib import admin
from mainpage.models import special_activities_tab,activity_records_count

class special_activities_admin(admin.ModelAdmin):
    list_display = ('title','content','image')

class activity_records_admin(admin.ModelAdmin):
    list_display = ('years', 'applicants','members','projects')

admin.site.register(special_activities_tab)
admin.site.register(activity_records_count)