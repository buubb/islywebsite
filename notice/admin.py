# admin.py
from django.contrib import admin
from .models import AttendanceLink, SubmissionLink, RentalLink, Lecture, Hashtag, Fee
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple


@admin.register(AttendanceLink)
class AttendanceLinkAdmin(admin.ModelAdmin):
    list_display = ["link"]

    def save_model(self, request, obj, form, change):
        AttendanceLink.objects.all().delete()
        super().save_model(request, obj, form, change)


@admin.register(SubmissionLink)
class SubmissionLinkAdmin(admin.ModelAdmin):
    list_display = ["link"]

    def save_model(self, request, obj, form, change):
        SubmissionLink.objects.all().delete()
        super().save_model(request, obj, form, change)


@admin.register(RentalLink)
class RentalLinkAdmin(admin.ModelAdmin):
    list_display = ["link"]

    def save_model(self, request, obj, form, change):
        RentalLink.objects.all().delete()
        super().save_model(request, obj, form, change)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ["link", "title", "display_hashtags", "thumbnail"]

    formfield_overrides = {ManyToManyField: {"widget": CheckboxSelectMultiple}}

    def display_hashtags(self, obj):
        return ', '.join(hashtag.name for hashtag in obj.hashtags.all())
    display_hashtags.short_description = "Hashtags"


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ["membership_fee", "extension_fee"]

    def save_model(self, request, obj, form, change):
        Fee.objects.all().delete()
        super().save_model(request, obj, form, change)