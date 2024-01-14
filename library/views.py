from django.shortcuts import render, get_object_or_404, redirect
from .models import LibraryPost, LibraryComment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# 목록 페이지를 부르는 Library 함수
def Library(request):
    page = request.GET.get('page', '1')
    # 모든 Post를 가져와 postlist에 저장합니다
    library_list = LibraryPost.objects.order_by('-created_date')

    # 페이징 처리
    paginator = Paginator(library_list, 10)
    page_obj = paginator.get_page(page)
    context = {'library_list': page_obj}
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'library/library_list.html', context)

def posting(request, post_id):
    
    # 게시글(Post) 중 post_id를 이용해 하나의 게시글(post)를 검색
    librarypost = get_object_or_404(LibraryPost, pk=post_id)
    # 조회 횟수 증가
    librarypost.library_count += 1
    librarypost.save()
    context = {'post': librarypost}
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'library/library_posting.html', context)
    
@login_required(login_url='common:login') #나중에 로그인 링크 수정하기
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            librarypost = form.save(commit=False)
            librarypost.author = request.user
            librarypost.create_date = timezone.now()
            librarypost.save()
            return redirect('Library')
    else: 
        form = PostForm()
    context = {'form': form}
    return render(request, 'library/library_write.html', context)

def post_modify(request, post_id):
    librarypost = get_object_or_404(LibraryPost, pk=post_id)
    if request.user != librarypost.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('posting', post_id = librarypost.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=librarypost)
        if form.is_valid():
            librarypost = form.save(commit=False)
            librarypost.modify_date = timezone.now()  # 수정일시 저장
            librarypost.save()
            return redirect('posting', post_id = librarypost.id)
    else:
        form = PostForm(instance=librarypost)
    context = {'form': form}
    return render(request, 'library/library_write.html', context)

@login_required(login_url='common:login')
def post_delete(request, post_id):
    librarypost = get_object_or_404(LibraryPost, pk=post_id)
    if request.user != librarypost.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('posting', post_id = librarypost.id)
    librarypost.delete()
    return redirect('Library')


@login_required(login_url='common:login') 
def comment_create_library(request, post_id):
    librarypost = get_object_or_404(LibraryPost, pk=post_id) 
    if request.method == 'POST':
        form = CommentForm(request.POST) 
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.author = request.user 
            comment.create_date = timezone.now() 
            comment.librarypost = librarypost
            comment.save()
            return redirect('posting', post_id = librarypost.id)
    else:
        form = CommentForm()
        context = {'form':form}
        return render(request, 'library/comment_form.html', context)
    
@login_required(login_url='common:login') 
def comment_modify_library(request, comment_id):
    comment = get_object_or_404(LibraryComment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('posting', post_id=comment.librarypost.id )
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment) 
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.author = request.user 
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('posting', post_id=comment.librarypost.id)
        else:
            form = CommentForm(instance=comment)
        context = {'form':form}
        return render(request, 'library/comment_form.html', context)
    
@login_required(login_url='common:login') 
def comment_delete_library(request, comment_id):
    comment = get_object_or_404(LibraryComment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('posting', post_id=comment.librarypost.id )
    else:
        comment.delete()
    return redirect('posting', post_id=comment.librarypost.id )
