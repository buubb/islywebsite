from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from volunteer.models import Post
from django.contrib.humanize.templatetags.humanize import ordinal
from django.contrib.auth.decorators import login_required


def feed(request):
    # 처음에 보여줄 포스트 개수
    initial_post_count = 6

    # 처음에 보여줄 포스트 데이터 조회
    posts = Post.objects.all().order_by("-generation")[:initial_post_count]

    context = {"posts": posts}
    return render(request, "volunteer/feed.html", context)


def load_more(request):
    # 현재까지 보여준 포스트의 개수를 받아옴
    current_count = int(request.GET.get("current_count", 0))

    # 추가로 불러올 포스트 개수
    load_count = 6

    # 새로 불러올 포스트
    additional_posts = Post.objects.all().order_by("-generation")[current_count:current_count + load_count]

    # 포스트 정보를 JSON으로 변환하여 반환
    data = []
    for post in additional_posts:
        data.append({
            "id": post.id,
            "generation_ordinal": ordinal(post.generation),  # 서수 변환 적용
            "year": post.year,
            "title": post.title,
            "like_count": post.like_users.count(),
            "image_url": post.postimage_set.first().photo.url if post.postimage_set.first() else "/static/volunteer/images/default-image.png",
        })

    no_more_posts = current_count + load_count >= Post.objects.count()

    return JsonResponse({"posts": data, "no_more_posts": no_more_posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    all_posts = Post.objects.exclude(id=post_id).order_by("-created")

    context = {
        "post": post,
        "all_posts": all_posts,
    }
    return render(request, "volunteer/post_detail.html", context)


@login_required(login_url="login")
def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    # 사용자가 "좋아요를 누른 Post 목록"에 "좋아요 버튼을 누른 Post"가 존재한다면
    if user.like_posts.filter(id=post.id).exists():
        # 좋아요 목록에서 삭제한다
        user.like_posts.remove(post)
    # 존재하지 않는다면 좋아요 목록에 추가한다
    else:
        user.like_posts.add(post)

    # next로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 해당 Post 위치로 이동한다
    url_next = request.GET.get("next") or reverse("Volunteer:post_detail", args=[post_id])

    return HttpResponseRedirect(url_next)