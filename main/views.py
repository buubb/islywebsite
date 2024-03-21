# backend
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
#from main.models import SpecialActivitiesPost, ActivityRecordsCount
from django.views import View

class Main(View):
    def post(self, request):
        print("post로 호출")
        return render(request, 'main/index.html')
    def get(self,request):
        return render(request, 'main/index.html')
        # SpecialActivities model과 연결
        # sapPost = SpecialActivitiesPost.objects.all()
        # ActivityRecords model과 연결 
        #records = ActivityRecordsCount.objects.all()
        # main/index.html에서 적용할 수 있도록 render
        #return render(request,"main/index.html",({"sapPost":sapPost, "records":records}))
    

        
