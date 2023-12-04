# backend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from typing import Any
from django.views.generic.edit import CreateView
from .forms import TeamActivitiesForm
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from django.views.generic import ListView
from .models import TeamActivitiesPost

def TeamWebPosting(request, post_id):
    #게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post=get_object_or_404(TeamActivitiesPost, id=post_id)

    #조회 횟수 증가
    post.hits += 1
    post.save()

    #작성자 정보 가져오기
    author = post.author

    #페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'team_activities/teampost.html',{'TeamActivitiesPost':post, 'author':author})

def TeamRevPosting(request, post_id):
    #게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post=get_object_or_404(TeamActivitiesPost, id=post_id)

    #조회 횟수 증가
    post.hits += 1
    post.save()

    #작성자 정보 가져오기
    author = post.author

    #페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'team_activities/teampost.html',{'post':post, 'author':author})

def TeamPwnPosting(request, post_id):
    #게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post=get_object_or_404(TeamActivitiesPost, id=post_id)

    #조회 횟수 증가
    post.hits += 1
    post.save()

    #작성자 정보 가져오기
    author = post.author

    #페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'team_activities/teampost.html',{'post':post, 'author':author})

def TeamAdvPosting(request, post_id):
    #게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post=get_object_or_404(TeamActivitiesPost, id=post_id)

    #조회 횟수 증가
    post.hits += 1
    post.save()

    #작성자 정보 가져오기
    author = post.author

    #페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'team_activities/teampost.html',{'post':post, 'author':author})

"""class TeamActivities(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'team_activities/team_list.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'team_activities/team_list.html')
"""
    
class TeamWritePage(LoginRequiredMixin,CreateView):
    model = TeamActivitiesPost
    form_class=TeamActivitiesForm
    template_name = "team_activities/teamboard.html"
    success_url = reverse_lazy('team_list')

    def form_valid(self,form):
        #현재 로그인한 사용자를 작성자로 설정
        form.instance.author= self.request.user
        return super().form_valid(form)
    
class TeamActivitiesView(ListView):
    model=TeamActivitiesPost
    paginate_by= 10
    template_name='team_activities/team_list.html' #DEFAULT: <app_label>/<model_name>_list.html
    context_object_name= 'team_list' #DEFAULT: <model_name>_list

    def get_queryset(self):
        team_list = TeamActivitiesPost.objects.order_by('-id')
        return team_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page=self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index= start_index + page_numbers_range
        if end_index >= max_index:
            end_index=max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context