# backend
from django.shortcuts import render
from .models import Recruitment, Announcement
import datetime


def recruit(request):
    recruitment = Recruitment.objects.first()
    announcement = Announcement.objects.first()
    today = datetime.date.today()

    # 합격 발표 기간
    if announcement and announcement.start_date <= today <= announcement.end_date:
        return render(request, "recruit/status.html")

    # 모집 기간
    if recruitment and recruitment.start_date <= today <= recruitment.end_date:
        return render(request, "recruit/recruit.html", {"application_link": recruitment.application_link})

    # 그 외 기간
    return render(request, "recruit/recruit.html", {"not_in_recruitment_period": True})


def status(request):
    return render(request, "recruit/status.html")