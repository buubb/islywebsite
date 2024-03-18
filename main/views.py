# backend
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from main.models import SpecialActivitiesPost
from django.views import View

class Main(View):
    def post(self, request):
        print("post로 호출")
        return render(request, 'main/index.html')
    def get(self,request):
        sapPost = SpecialActivitiesPost.objects.all()
        return render(request,"main/index.html",({"sapPost":sapPost}))
    

        
