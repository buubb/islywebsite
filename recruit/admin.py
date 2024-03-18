# admin.py
from django.contrib import admin
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.db import models
from .models import Recruitment, Announcement


class BaseDateAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput(attrs={'type': 'date'})},
    }

    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            form.add_error(None, e)


class RecruitmentAdmin(BaseDateAdmin):
    list_display = ('start_date', 'end_date', 'application_link')


class AnnouncementAdmin(BaseDateAdmin):
    list_display = ('start_date', 'end_date')


admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)