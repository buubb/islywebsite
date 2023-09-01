# backend
from django.shortcuts import render, get_object_or_404

# View에 Model(Post 게시글) 가져오기
from .models import BasicAssignment

def BasicBlog(request):
    postlist = BasicAssignment.objects.all()
    return render(request, 'assignments/basiclist.html',{'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, post_id):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = get_object_or_404(BasicAssignment, id=post_id)
    # 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'assignment/tem2.html', {'post':post})