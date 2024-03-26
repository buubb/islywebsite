# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import LoginFail
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse

LOGIN_TRY_LIMIT=5

class Login(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            return render(request, 'islyweb/index.html')
        else:
            form=AuthenticationForm()
            return render(request, 'login/new2.html', {'form':form})
            
    
    def post(self, request):
        print("post로 호출")
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user_instance = get_user_model().objects.get(username=username)
            user=authenticate(username=username, password=password)
            
            next = request.POST["next"]

            if user is not None: #사용자가 인증되었는지 확인
                print(user)
                LoginFail.objects.filter(user__username=username).delete()
                    
                login(request, user)
                return redirect(next)
                # return render(request, 'islyweb/index.html')
            else:
                # 로그인 실패 기록 가져오기
                if LoginFail.objects.filter(user__username=username).exists():
                    login_fail = LoginFail.objects.get_or_create(user=user_instance, defaults={"count": 0})[0]
                    count = login_fail.count
                else:
                    count = 0
        else:
            return redirect(reverse("login"))


class Logout(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            Logout(request)
            return render(request, 'islyweb/index.html')


from django.http import HttpResponse

def check_session_status(request):
    if request.user.is_authenticated:
        return 
    else:
        return HttpResponse('세션이 만료되었습니다. 다시 로그인해주세요.')