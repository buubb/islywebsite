# admin.py
from django.contrib import admin
from .models import AttendanceLink, SubmissionLink, RentalLink, Rental, Hashtag


class AttendanceLinkAdmin(admin.ModelAdmin):
    list_display = ("link",)

    def save_model(self, request, obj, form, change):
        AttendanceLink.objects.all().delete()
        super().save_model(request, obj, form, change)


class SubmissionLinkAdmin(admin.ModelAdmin):
    list_display = ("link",)

    def save_model(self, request, obj, form, change):
        SubmissionLink.objects.all().delete()
        super().save_model(request, obj, form, change)


class RentalLinkAdmin(admin.ModelAdmin):
    list_display = ("link",)

    def save_model(self, request, obj, form, change):
        RentalLink.objects.all().delete()
        super().save_model(request, obj, form, change)


class RentalAdmin(admin.ModelAdmin):
    list_display = ("link", "title", "display_hashtags", "thumbnail")

    def display_hashtags(self, obj):
        return ', '.join(hashtag.name for hashtag in obj.hashtags.all())
    display_hashtags.short_description = "Hashtags"


admin.site.register(AttendanceLink, AttendanceLinkAdmin)
admin.site.register(SubmissionLink, SubmissionLinkAdmin)
admin.site.register(RentalLink, RentalLinkAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(Hashtag)