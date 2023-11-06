# backend
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic import ListView
from .models import TeamActivitiesPost

class TeamActivities(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'team_activities/team_list.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'team_activities/team_list.html')
    
class TeamWritePage(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'team_activities/teamboard.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'team_activities/teamboard.html')
    
class TeamActivitiesView(ListView):
    model=TeamActivitiesPost
    paginate_by= 3
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