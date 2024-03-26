# backend
from django.shortcuts import render
from rest_framework.views import APIView
from .models import AttendanceLink, SubmissionLink, RentalLink

class Notice(APIView):
    def get(self, request):
        print("get으로 호출")
        attendance_link = AttendanceLink.objects.first()
        submission_link = SubmissionLink.objects.first()
        rental_link = RentalLink.objects.first()  
        return render(request, "notice/notice.html", {"attendance_link": attendance_link, "submission_link": submission_link, "rental_link": rental_link})

    def post(self, request):
        print("post로 호출")
        attendance_link = AttendanceLink.objects.first()
        submission_link = SubmissionLink.objects.first()
        rental_link = RentalLink.objects.first()  
        return render(request, "notice/notice.html", {"attendance_link": attendance_link, "submission_link": submission_link, "rental_link": rental_link})
