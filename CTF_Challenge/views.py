# views.py
from django.shortcuts import render
from django.db.models import Count
from .models import Player


def wargame(request):
    players = Player.objects.annotate(same_point_count=Count('point')).order_by("-point")

    current_rank = 1
    prev_score = None
    for player in players:
        if player.point != prev_score:
            player.rank = current_rank
            current_rank += player.same_point_count
        else:
            player.rank = current_rank - 1
        prev_score = player.point

    context = {
        "players": players
    }
    return render(request, "CTF_Challenge/ctf.html", context)
