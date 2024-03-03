from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from volunteer.models import Post, Comment, PostImage
from volunteer.forms import CommentForm, PostForm
from django.contrib.humanize.templatetags.humanize import ordinal
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def feed(request):
    # 초기 포스트 개수
    initial_post_count = 6

    # 내림차순 정렬
    posts = Post.objects.all().order_by("-generation")[:initial_post_count]

    context = {"posts": posts}
    return render(request, "volunteer/feed.html", context)


def load_more(request):
    # 현재까지 보여준 포스트의 개수를 받아옴
    current_count = int(request.GET.get("current_count", 0))

    # 추가로 불러올 포스트 개수
    load_count = 6

    # 내림차순 정렬
    additional_posts = Post.objects.all().order_by("-generation")[current_count:current_count + load_count]

    # 포스트 정보를 JSON 형태로 변환
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

    # 추가로 불러올 포스트가 더 이상 없는지 확인
    no_more_posts = current_count + load_count >= Post.objects.count()

    return JsonResponse({"posts": data, "no_more_posts": no_more_posts})


@login_required(login_url="login")
def post_add(request):
    if request.method == "POST":
        # request.POST로 온 데이터는 PostForm으로 처리
        form = PostForm(request.POST)

        if form.is_valid():
            # Post의 "user"값은 request에서 가져와 자동할당
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # Post를 생성 한 후
            # request.FILES.getlist("images")로 전송된 이미지들을 순회하며 PostImage객체를 생성
            for image_file in request.FILES.getlist("images"):
                # request.FILES또는 request.FILES.getlist()로 가져온 파일은
                # Model의 ImageField부분에 곧바로 할당
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )

            # 모든 PostImage와 Post의 생성이 완료되면
            # 해당 Post의 상세페이지로 이동
            url = reverse("Volunteer:post_detail", args=[post.id])
            return redirect(url)

    # GET요청일 때는 빈 form을 보여주기
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, "volunteer/post_add.html", context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    all_posts = Post.objects.exclude(id=post_id).order_by("generation")  # 오름차순 정렬

    context = {
        "post": post,
        "all_posts": all_posts,
    }
    return render(request, "volunteer/post_detail.html", context)


@login_required(login_url="login")
def post_delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id)

        # 권한 확인
        if request.user != post.user:
            # 작성자가 아닌 경우
            messages.error(request, 'You do not have permission to delete this post')
            return redirect('Volunteer:post_detail', post_id=post_id)

        # 사용자가 게시물을 삭제할 수 있는 권한이 있는 경우
        post.delete()

        # 삭제 후 피드 페이지로 이동
        return redirect('Volunteer:feed')

    except Post.DoesNotExist:
        # 해당 ID의 게시물이 존재하지 않는 경우
        return render(request, 'volunteer/404_2.html')


@login_required(login_url="login")
def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    # 사용자가 "좋아요를 누른 Post 목록"에 "좋아요 버튼을 누른 Post"가 존재한다면
    if user.like_posts.filter(id=post.id).exists():
        # 좋아요 목록에서 삭제
        user.like_posts.remove(post)
    # 존재하지 않는다면 좋아요 목록에 추가
    else:
        user.like_posts.add(post)

    # next로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 해당 Post 위치로 이동
    url_next = request.GET.get("next") or reverse("Volunteer:post_detail", args=[post_id])

    return redirect(url_next)