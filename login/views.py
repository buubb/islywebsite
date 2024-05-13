# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages
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

        if request.user.is_authenticated:
            return render(request, 'mainpage/index.html')
        else:
            form = AuthenticationForm()
            # messages = get_messages(request)
            return render(request, 'login/new3.html')

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)

        # 사용자의 IP 주소 가져오기
        user_ip = self.get_client_ip(request)
        
        # 로그인 시도 횟수 가져오기
        login_attempts = cache.get(user_ip, 0)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                cache.delete(user_ip) 
                login(request, user)
                next_url = request.POST.get('next', '')

                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('mainpage:index')  # 로그인 성공 시 메인 페이지로 이동
            else:
                # 로그인 실패 시 시도횟수 +1 후 캐시에 저장
                login_attempts += 1
                cache.set(user_ip, login_attempts, timeout=1800)
                return render(request, 'login/new3.html')
        else:
            # 로그인 실패 시 시도횟수 +1 후 캐시에 저장
            login_attempts += 1
            cache.set(user_ip, login_attempts, timeout=1800)
            return render(request, 'login/new3.html')
        
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
    
class CheckLogin(APIView):
    def get(self, request):
        form = AuthenticationForm()
        if request.user.is_authenticated:
            return render(request, 'mainpage/index.html')
        else:
            return render(request, 'login/check.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('change_password')
            else:
                return render(request, 'login/check.html', {'form': form})
        else:
            return render(request, 'login/check.html', {'form': form})
        
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .validators import CustomPasswordValidator


def change_password(request):
    if request.method == "POST":
        user = request.user
        origin_password = request.POST.get("origin_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # 현재 비밀번호 확인
        if not check_password(origin_password, user.password):
            # messages.error(request, 'Current password is incorrect.')
            return render(request, 'login/change_password.html')
            # return render(request, 'login/change_password.html', {'message': error})

        # 신규 비밀번호 확인
        if new_password != confirm_password:
            # messages.error(request, 'Passwords do not match.')
            return render(request, 'login/change_password.html')
            # return render(request, 'login/change_password.html', {'message': error})
        
        # 비밀번호 유효성 검사
        try:
            validate_password(new_password, user=user)
        except ValidationError as error:
            # messages.error(request, str(error))
            return render(request, 'login/change_password.html')
        
        # 사용자 정의 비밀번호 유효성 검사 규칙을 적용
        custom_validator = CustomPasswordValidator()
        try:
            custom_validator.validate(new_password, user=user)
        except ValidationError as error:
            # messages.error(request, 'try again')
            return render(request, 'login/change_password.html')
        
        # 비밀번호 변경
        user.set_password(new_password)
        user.save()
        logout(request)
        login(request, user)
        return render(request, 'mainpage/index.html')
    else:
        return render(request, 'login/change_password.html')