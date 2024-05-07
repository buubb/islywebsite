# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import get_messages
# from .models import ConcurrentLogin
from django.core.cache import cache
import ipaddress

LOGIN_TRY_LIMIT=5


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_list = x_forwarded_for.split(',')
        client_ip = ip_list[0].strip()
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    
    # IPv6 주소인 경우 "::ffff:"가 포함되어 있을 수 있으므로 제거
    if client_ip.startswith('::ffff:'):
        client_ip = client_ip[7:]
    
    # IPv4 주소가 맞는지 확인
    try:
        ipaddress.IPv4Address(client_ip)
    except ipaddress.AddressValueError:
        client_ip = None
    
    return client_ip

class Login(APIView):
    def get(self, request):
        form = AuthenticationForm()

         # 사용자의 IP 주소 가져오기
        client_ip = get_client_ip(request)

        # 로그인 시도 횟수 가져오기
        login_attempts = cache.get(client_ip, 0)
        context = { 'client_ip': client_ip, 'login_attempts': login_attempts}
       
        if request.user.is_authenticated:
            return render(request, 'mainpage/index.html')
        else:
            form = AuthenticationForm()
            # messages = get_messages(request)
            return render(request, 'login/new3.html', context)

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)

        # 사용자의 IP 주소 가져오기
        client_ip = get_client_ip(request)
        
        # 로그인 시도 횟수 가져오기
        login_attempts = cache.get(client_ip, 0)

        context = { 'client_ip': client_ip, 'login_attempts': login_attempts}

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # 로그인 성공 시 캐시 값 삭제
                cache.delete(client_ip)
                next_url = request.POST.get('next', '')
                if next_url:
                    return redirect(next_url)
                else:
                    return render(request, 'mainpage/index.html')  # 로그인 성공 시 메인 페이지로 이동
            else:
                # 로그인 실패 시 시도횟수 +1 후 캐시에 저장
                login_attempts += 1
                cache.set(client_ip, login_attempts, timeout=None)
                # messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
                return render(request, 'login/new3.html', context)
                # return redirect('login')  # 로그인 실패 시 로그인 페이지로 리다이렉트
        else:
            # 로그인 실패 시 시도횟수 +1 후 캐시에 저장
            login_attempts += 1
            cache.set(client_ip, login_attempts, timeout=None)
            # messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
            return render(request, 'login/new3.html', context)
            # return redirect('login')  # 폼이 유효하지 않을 때 로그인 페이지로 리다이렉트
        
class Logout(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            Logout(request)
            return render(request, 'mainpage/index.html')
        
    def post(self, request):
        print("post으로 호출")
        if request.user.is_authenticated:
            Logout(request)
            return render(request, 'mainpage/index.html')


def check_session_status(request):
    if request.user.is_authenticated:
        return
    else:
        return HttpResponse('세션이 만료되었습니다. 다시 로그인해주세요.')