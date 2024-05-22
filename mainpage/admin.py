from django.contrib import admin
from mainpage.models import special_activities_tab,activity_records_count, InstagramToken

class special_activities_admin(admin.ModelAdmin):
    list_display = ('subtitle','title','content','category')

class activity_records_admin(admin.ModelAdmin):
    list_display = ('years', 'applicants','members','projects')

class InstagramToken_admin(admin.ModelAdmin):
    list_display = ('token', 'last_updated')

admin.site.register(special_activities_tab)
admin.site.register(activity_records_count)
admin.site.register(InstagramToken)