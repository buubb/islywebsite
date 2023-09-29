from django.shortcuts import render, get_object_or_404, redirect
from .models import LibraryPost
from .forms import PostForm
from django.utils import timezone
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required

# 목록 페이지를 부르는 Library 함수
def Library(request):
    page = request.GET.get('page', '1')
    # 모든 Post를 가져와 postlist에 저장합니다
    post_list = LibraryPost.objects.order_by('-created_date')

    # 페이징 처리
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'library/tem2.html', context)

def posting(request, post_id):
    # 게시글(Post) 중 post_id를 이용해 하나의 게시글(post)를 검색
    post = get_object_or_404(LibraryPost, pk=post_id)
    context = {'post': post}
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'library/posting.html', context)
    
@login_required(login_url='common:login') #나중에 로그인 링크 수정하기
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('Library')
    else: 
        form = PostForm()
    context = {'form':form}
    return render(request, 'library/library_write.html', context)
