from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

LOGIN_FAILED_IP_COUNT = 10

class Login(APIView):

    def get(self, request):
        form = AuthenticationForm()
        if request.user.is_authenticated:
            return render(request, 'mainpage/index.html')
        else:
            return render(request, 'login/new3.html')

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)

        # 세션에서 로그인 시도 횟수 가져오기
        attempt = request.session.get('login_attempt', 0)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', '')

                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('mainpage:index')  # 로그인 성공 시 메인 페이지로 이동
            else:
                return render(request, 'login/new3.html')
        else:
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

@login_required
def password_edit_view(request):
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        
        if request.user.is_authenticated:
            if password_change_form.is_valid():
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                return render(request, 'mainpage/index.html')
            else:
                return render(request, 'login/change_password.html', {'password_change_form':password_change_form})
        else:
            return render(request, 'mainpage/index.html')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'login/change_password.html', {'password_change_form':password_change_form})