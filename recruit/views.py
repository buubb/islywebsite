# backend
from django.shortcuts import render
from .models import Recruitment, Announcement, Applicant
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


def check_status(request):
    phone_number = request.POST.get("applicant_phone")
    try:
        applicant = Applicant.objects.get(phone_number=phone_number)
        if applicant.is_passed:
            return render(request, "recruit/pass.html", {"name": applicant.name})  # 합격자인 경우 pass.html로 리다이렉트
        else:
            return render(request, "recruit/fail.html", {"name": applicant.name})  # 불합격자인 경우 fail.html로 리다이렉트
    except Applicant.DoesNotExist:
        return render(request, "recruit/status.html", {"not_in_recruitment_period": True})