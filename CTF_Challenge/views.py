# views.py
from django.shortcuts import render
from .models import Player


def ctf(request):
    players = Player.objects.all()
    context = {
        "players": players
    }
    return render(request, "CTF_Challenge/ctf.html", context)