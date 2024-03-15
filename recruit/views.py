# backend
from django.shortcuts import render
from .models import Recruitment
import datetime


def recruit(request):
    recruitment = Recruitment.objects.first()
    today = datetime.date.today()
    if recruitment and recruitment.start_date <= today <= recruitment.end_date:
        return render(request, "recruit/recruit.html", {"application_link": recruitment.application_link})
    else:
        return render(request, "recruit/recruit.html", {"not_in_recruitment_period": True})


def status(request):
    return render(request, "recruit/status.html")