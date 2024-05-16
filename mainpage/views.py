# backend
import json, requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from mainpage.models import special_activities_tab,activity_records_count, InstagramToken
from django.views import View
from django.utils import timezone

class Main(View):
    def post(self, request):
        print("post로 호출")
        return render(request, 'mainpage/index.html')
    def get(self,request):
        special_acts = special_activities_tab.objects.all().order_by('-id')[:4]
        act_records = activity_records_count.objects.all().order_by('-id')[:1]

        context = {
            'special_acts':special_acts,
            'act_records':act_records
        }
        return render(request, 'mainpage/index.html', context)
    
        
def get_instagram_token(request):
    token_object = InstagramToken.objects.last()  # 가장 최근에 저장된 토큰을 가져옴
    return JsonResponse({'token': token_object.token})

def refresh_instragram_token(request):
    token = InstagramToken.objects.last()

    # 인스타그램 API 엔드포인트 및 파라미터 설정
    endpoint = 'https://graph.instagram.com/refresh_access_token'
    params = {
        'grant_type': 'ig_refresh_token',
        'access_token': token
    }

    # 인스타그램 API에 GET 요청 보내기
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        # 요청이 성공하면 새로운 토큰 값을 반환
        data = response.json()
        new_token = data.get('access_token', '')
        InstagramToken.objects.create(token=new_token)
        return JsonResponse({'new_token': new_token})
    else:
        # 요청이 실패하면 에러 메시지 반환
        error_message = response.json().get('error', 'Unknown error')
        return JsonResponse({'error': error_message}, status=response.status_code)
    
        