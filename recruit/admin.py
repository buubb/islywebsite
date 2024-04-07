# admin.py
from django.contrib import admin
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.db import models
from .models import Recruitment, Announcement, Applicant, Orientation, Discord, Contact


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


@admin.register(Recruitment)
class RecruitmentAdmin(BaseDateAdmin):
    list_display = ["start_date", "end_date", "application_link"]


@admin.register(Announcement)
class AnnouncementAdmin(BaseDateAdmin):
    list_display = ["start_date", "end_date"]


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ["generation", "position", "name", "student_id", "phone_number", "is_passed"]
    ordering = ["-generation"]


@admin.register(Orientation)
class OrientationAdmin(BaseDateAdmin):
    list_display = ["date", "type"]

    def save_model(self, request, obj, form, change):
        Orientation.objects.all().delete()
        super().save_model(request, obj, form, change)


@admin.register(Discord)
class DiscordAdmin(BaseDateAdmin):
    list_display = ["expire_after", "invite_link"]

    def save_model(self, request, obj, form, change):
        Discord.objects.all().delete()
        super().save_model(request, obj, form, change)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["contact"]

    def save_model(self, request, obj, form, change):
        Contact.objects.all().delete()
        super().save_model(request, obj, form, change)
