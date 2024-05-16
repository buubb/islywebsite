# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Player
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


def calculate_rank(all_players):
    current_rank = 1
    prev_score = None
    for player in all_players:
        if player.point != prev_score:
            player.rank = current_rank
            current_rank += player.same_point_count
        else:
            player.rank = current_rank - 1
        prev_score = player.point


def paginate_players(request, all_players):
    paginator = Paginator(all_players, 7)

    page_number = request.GET.get("page")
    try:
        players = paginator.page(page_number)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages)

    return players


def wargame(request):
    # 전체 플레이어 정보
    all_players = Player.objects.annotate(same_point_count=Count('point')).order_by("-point")

    # 현재 로그인한 사용자의 정보
    if request.user.is_authenticated:
        user_player = all_players.filter(user=request.user).order_by("-updated").first()
    else:
        user_player = None

    # 랭킹 계산
    calculate_rank(all_players)

    # 페이지네이션
    players = paginate_players(request, all_players)

    context = {
        "players": players,
        "all_players": all_players,
        "user_player": user_player,
    }
    return render(request, "CTF_Challenge/wargame.html", context)


@login_required(login_url="login")
def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user
            player.save()
            return redirect("CTFChallenge:wargame")
    else:
        form = PlayerForm()

    context = {"form": form}
    return render(request, "CTF_Challenge/player_form.html", context)


@login_required(login_url="login")
def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)

    if request.user != player.user:
        messages.error(request, "You do not have permission to edit this stat.")
        return redirect("CTFChallenge:wargame")

    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            player = form.save(commit=False)
            player.updated = timezone.now()
            player.save()
            return redirect("CTFChallenge:wargame")
    else:
        form = PlayerForm(instance=player)

    context = {
        "form": form,
        "player": player,
    }
    return render(request, "CTF_Challenge/player_form.html", context)


def snake(request):
    return render(request, "CTF_Challenge/snake.html")


def flag(request):
    return render(request, "CTF_Challenge/flag.html")
