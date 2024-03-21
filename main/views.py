# backend
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from main.models import special_activities_tab,activity_records_count
from django.views import View

class Main(View):
    def post(self, request):
        print("post로 호출")
        return render(request, 'main/index.html')
    def get(self,request):
        special_acts = special_activities_tab.objects.all().order_by('-id')[:4]
        act_records = activity_records_count.objects.all().order_by('-id')[:1]

        context = {
            'special_acts':special_acts,
            'act_records':act_records
        }
        return render(request, 'main/index.html', context)
    
        

        
