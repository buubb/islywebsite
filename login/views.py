# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import LoginFail
from django.contrib.auth import get_user_model

LOGIN_TRY_LIMIT=5

class Login(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            return render(request, 'islyweb/index.html')
        else:
            form=AuthenticationForm()
            return render(request, 'login/make.html', {'form':form})
            
    
    def post(self, request):
        print("post로 호출")
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            
            if user is not None:
                print(user)
                LoginFail.objects.filter(user__username=username).delete()
                login(request, user)
                return render(request, 'islyweb/index.html')
            else:
                # 로그인 실패 기록 가져오기
                if LoginFail.objects.filter(user__username=username).exists():
                    login_fail = LoginFail.objects.get(user__username=username)
                    count = login_fail.count
                else:
                    count = 0

                if count >= LOGIN_TRY_LIMIT:
                    # 로그인 실패횟수 초과로 인해 잠긴 계정에 대한 인증 시도 제한
                    return render(request, "account_lock.html", {"state": "account_lock"})
                else:
                    user_instance = get_user_model().objects.get(username=username)
                    LoginFail.objects.update_or_create(
                    user=user_instance,
                    defaults={"count": count + 1},
                    )
                    return render(request, "login_failed.html", {"state": "login_failed"})
        else:
            return render(request, 'login/make.html')


class Logout(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            Logout(request)
        return render(request, 'islyweb/index.html')



