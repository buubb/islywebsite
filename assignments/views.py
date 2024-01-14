# backend
from django.shortcuts import render, get_object_or_404, redirect
from .models import BasicAssignment, AdvancedAssignment
from .forms import AdvancedAssignmentForm, BasicAssignmentForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def BasicList(request):
    postlist1 = BasicAssignment.objects.order_by('-created_at')

    paginator = Paginator(postlist1, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'assignments/basiclist.html', {'page': page})

def AdvancedList(request):
    # AdvancedAssignment 모델의 모든 게시물을 가져와서 'created_at' 필드를 기준으로 내림차순 정렬합니다.
    postlist2 = AdvancedAssignment.objects.all().order_by('-created_at')

    paginator = Paginator(postlist2, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'assignments/advancedlist.html', {'page': page})


# blog의 게시글(posting)을 부르는 posting 함수
# BasicPosting
def BasicPosting(request, post_id):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = get_object_or_404(BasicAssignment, id=post_id)

    # 조회 횟수 증가
    post.view_count += 1
    post.save()

    # 작성자 정보 가져오기
    author = post.author
    # 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'assignments/post.html', {'post': post, 'author': author})

def AdvancedPosting(request, post_id):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = get_object_or_404(AdvancedAssignment, id=post_id)

    # 조회 횟수 증가
    post.view_count += 1
    post.save()

    # 작성자 정보 가져오기
    author = post.author
    # 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'assignments/post.html', {'post': post, 'author': author})

@login_required(login_url='common:login')
def BasicCreate(request):
    if request.method == 'POST':
        form = BasicAssignmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_at = timezone.now()
            post.save()
            return redirect('basic')
    else:
        form = BasicAssignmentForm()

    context = {'form': form}
    return render(request, 'assignments/submit.html', context)

@login_required(login_url='common:login')
def AdvancedCreate(request):
    if request.method == 'POST':
        form = AdvancedAssignmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_at = timezone.now()
            post.save()
            return redirect('advanced')
    else:
        form = AdvancedAssignmentForm()

    context = {'form': form}
    return render(request, 'assignments/submit.html', context)