# backend
from django.shortcuts import render

def recruit(request):
    return render(request, 'recruit/recruit.html')

def status(request):
    return render(request, "recruit/status.html")
