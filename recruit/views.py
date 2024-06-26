# backend
from django.shortcuts import render, get_object_or_404
from .models import Recruitment, Announcement, Applicant, Orientation, Discord, Contact
import datetime
from django.http import JsonResponse


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


def check_phone_number(request):
    if "phone_number" in request.GET:
        phone_number = request.GET["phone_number"]
        if Applicant.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({"exists": True})
    return JsonResponse({"exists": False})


def check_student_id(request):
    if "student_id" in request.GET and "phone_number" in request.GET:
        student_id = request.GET["student_id"]
        phone_number = request.GET["phone_number"]
        if Applicant.objects.filter(student_id=student_id, phone_number=phone_number).exists():
            applicant = Applicant.objects.get(student_id=student_id, phone_number=phone_number)
            return JsonResponse({"exists": True, "is_passed": applicant.is_passed})
    return JsonResponse({"exists": False})


def pass_page(request):
    student_id = request.GET.get("student_id")
    phone_number = request.GET.get("phone_number")

    applicant = get_object_or_404(Applicant, student_id=student_id, phone_number=phone_number)
    orientation = Orientation.objects.last()
    discord = Discord.objects.last()
    contact = Contact.objects.last()

    context = {
        "applicant": applicant,
        "orientation": orientation,
        "discord": discord,
        "contact": contact,
    }

    return render(request, "recruit/pass.html", context)


def fail_page(request):
    student_id = request.GET.get("student_id")
    phone_number = request.GET.get("phone_number")

    applicant = get_object_or_404(Applicant, student_id=student_id, phone_number=phone_number)

    context = {
        "applicant": applicant
    }
    return render(request, "recruit/fail.html", context)