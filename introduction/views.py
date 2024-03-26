# backend
from django.shortcuts import render


def introduction(request):
    return render(request, "introduction/brief.html")


def bylaws(request):
    return render(request, "introduction/rules.html")


def developers(request):
    return render(request, "introduction/dev.html")