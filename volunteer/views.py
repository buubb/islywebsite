from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView
from volunteer.models import Post
from django.core.paginator import Paginator


class Volunteer(APIView):
    def get(self, request):
        print("get으로 호출")
        posts = Post.objects.all()

        # Paging
        per_page = 2
        paginator = Paginator(posts, per_page)
        page_number = request.GET.get("page")  # Get the current page number
        posts = paginator.get_page(page_number)  # Retrieve the list of posts for the requested page

        # Sidebar
        all_posts = Post.objects.all()

        context = {"posts": posts, "page_number": page_number, "all_posts": all_posts}
        return render(request, "volunteer/feed.html", context)

    def post(self, request):
        print("post로 호출")
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, "volunteer/feed.html", context)


def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse("login") + f"?next={request.path}")

    if user.like_posts.filter(id=post.id).exists():
        user.like_posts.remove(post)
    else:
        user.like_posts.add(post)

    page_number = request.GET.get("page")

    url_next = request.GET.get("next") or reverse("Volunteer:volunteer") + f"?page={page_number}#post-{post.id}"
    return HttpResponseRedirect(url_next)