from django.contrib import admin
from main.models import SpecialActivitiesPost
class SpecialActivitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

    
admin.site.register(SpecialActivitiesPost)