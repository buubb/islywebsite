# admin.py
from django.contrib import admin
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.db import models
from .models import Recruitment, Announcement, Applicant, Orientation, Discord


class BaseDateAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {"widget": DateInput(attrs={"type": "date"})},
    }

    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            form.add_error(None, e)


class RecruitmentAdmin(BaseDateAdmin):
    list_display = ("start_date", "end_date", "application_link")


class AnnouncementAdmin(BaseDateAdmin):
    list_display = ("start_date", "end_date")


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("generation", "position", "name", "student_id", "phone_number", "is_passed")
    ordering = ["-generation"]


class OrientationAdmin(BaseDateAdmin):
    list_display = ("date", "type")

    def save_model(self, request, obj, form, change):
        Orientation.objects.all().delete()
        super().save_model(request, obj, form, change)


class DiscordAdmin(BaseDateAdmin):
    list_display = ("expire_after", "invite_link")

    def save_model(self, request, obj, form, change):
        Discord.objects.all().delete()
        super().save_model(request, obj, form, change)


admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Orientation, OrientationAdmin)
admin.site.register(Discord, DiscordAdmin)