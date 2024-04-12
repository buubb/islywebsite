# views.py
from django.shortcuts import render
from .models import Player


def ctf(request):
    players = Player.objects.order_by("-point")

    current_rank = 1
    prev_score = None
    for player in players:
        if player.point != prev_score:
            player.rank = current_rank
        else:
            player.rank = current_rank - 1
        prev_score = player.point
        current_rank += 1

    context = {
        "players": players
    }
    return render(request, "CTF_Challenge/ctf.html", context)