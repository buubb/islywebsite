from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from volunteer.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def feed(request):
    posts = Post.objects.all().order_by('-created')

    # Paging
    per_page = 8
    paginator = Paginator(posts, per_page)
    page_number = request.GET.get("page")  # Get the current page number
    posts = paginator.get_page(page_number)  # Retrieve the list of posts for the requested page

    context = {"posts": posts, "page_number": page_number}
    return render(request, "volunteer/feed.html", context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    all_posts = Post.objects.exclude(id=post_id).order_by('-created')

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