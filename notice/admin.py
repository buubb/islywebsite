# admin.py
from django.contrib import admin
from .models import AttendanceLink, SubmissionLink, RentalLink

admin.site.register(AttendanceLink)
admin.site.register(SubmissionLink)
admin.site.register(RentalLink)
