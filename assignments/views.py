# backend
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import BasicAssignment, AdvancedAssignment
from .forms import AdvancedAssignmentForm, BasicAssignmentForm
from django.core.paginator import Paginator

def BasicBlog(request):
    postlist1 = BasicAssignment.objects.order_by('-created_at')
    paginator = Paginator(postlist1, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'assignments/basiclist.html', {'page': page})

def AdvancedBlog(request):
    # AdvancedAssignment 모델의 모든 게시물을 가져와서 'created_at' 필드를 기준으로 내림차순 정렬합니다.
    postlist2 = AdvancedAssignment.objects.all().order_by('-created_at')

    # Paginator 객체를 생성하고 한 페이지당 10개의 아이템을 표시합니다.
    paginator = Paginator(postlist2, 10)
    # 클라이언트 요청에서 현재 페이지 번호를 가져옵니다.
    page_number = request.GET.get('page')
    # 요청된 페이지 번호로 페이지 객체를 가져옵니다.
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

class BasicCreate(CreateView):
    model = BasicAssignment
    form_class = BasicAssignmentForm
    template_name = 'assignments/submit.html'  # 기본 템플릿 설정
    success_url = reverse_lazy('basic')  # 성공 시 리디렉션할 URL 지정

class AdvancedCreate(CreateView):
    model = AdvancedAssignment
    form_class = AdvancedAssignmentForm  # 사용할 폼 클래스 설정
    template_name = 'assignments/submit.html'  # 기본 템플릿 설정
    success_url = reverse_lazy('advanced')  # 성공 시 리디렉션할 URL 지정





