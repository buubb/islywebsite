# backend
from django.shortcuts import render
from rest_framework.views import APIView

class TeamActivities(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'team_activities/index.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'team_activities/index.html')