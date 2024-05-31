# backend
from django.shortcuts import render
from notice.models import Fee


def introduction(request):
    return render(request, "introduction/brief.html")


def bylaws(request):
    fee = Fee.objects.last()
    context = {
        "fee": fee
    }
    return render(request, "introduction/rules.html", context)


def developers(request):
    return render(request, "introduction/dev.html")