# backend
from django.shortcuts import render, redirect
from .models import Recruitment, Announcement, Applicant
import datetime


def recruit(request):
    recruitment = Recruitment.objects.first()
    announcement = Announcement.objects.first()
    today = datetime.date.today()

    # 합격 발표 기간
    if announcement and announcement.start_date <= today <= announcement.end_date:
        # 전화번호 입력
        if request.method == 'POST':
            phone_number = request.POST.get('applicant_phone')
            try:
                applicant = Applicant.objects.get(phone_number=phone_number)
                if applicant.is_passed:
                    return render(request, "recruit/pass.html")
                else:
                    return render(request, "recruit/fail.html")
            except Applicant.DoesNotExist:
                return render(request, "recruit/status.html", {"not_in_recruitment_period": True})
        else:
            return render(request, "recruit/status.html")

    # 모집 기간
    if recruitment and recruitment.start_date <= today <= recruitment.end_date:
        return render(request, "recruit/recruit.html", {"application_link": recruitment.application_link})

    # 그 외 기간
    return render(request, "recruit/recruit.html", {"not_in_recruitment_period": True})