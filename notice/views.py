# backend
from django.shortcuts import render
from .models import AttendanceLink, SubmissionLink, RentalLink, Lecture


def notice(request):
    attendance_link = AttendanceLink.objects.last()
    submission_link = SubmissionLink.objects.last()
    rental_link = RentalLink.objects.last()
    lectures = Lecture.objects.all()

    context = {
        "attendance_link": attendance_link,
        "submission_link": submission_link,
        "rental_link": rental_link,
        "lectures": lectures,
    }
    return render(request, "notice/notice.html", context)