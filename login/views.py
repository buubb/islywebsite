# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import LoginFail
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.messages import get_messages
# from .models import ConcurrentLogin

LOGIN_TRY_LIMIT=5

class Login(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'mainpage/index.html')
        else:
            form = AuthenticationForm()
            messages = get_messages(request)
            return render(request, 'login/new3.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # ConcurrentLogin.objects.create(user=user, ip_address=request.META['REMOTE_ADDR'], user_agent=request.META['HTTP_USER_AGENT'])
                next_url = request.POST.get('next', '')
                if next_url:
                    return redirect(next_url)
                return render(request, 'mainpage/index.html')  # 로그인 성공 시 메인 페이지로 이동
            else:
                # messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
                return redirect('login')  # 로그인 실패 시 로그인 페이지로 리다이렉트
        else:
            # messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
            return redirect('login')  # 폼이 유효하지 않을 때 로그인 페이지로 리다이렉트

class Logout(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            Logout(request)
            return render(request, 'mainpage/index.html')

def check_session_status(request):
    if request.user.is_authenticated:
        return 
    else:
        return HttpResponse('세션이 만료되었습니다. 다시 로그인해주세요.')