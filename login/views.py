from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class Login(APIView):

    def get(self, request):
        form = AuthenticationForm()
        if request.user.is_authenticated:
            return render(request, 'mainpage/index.html')
        else:
            return render(request, 'login/new3.html')

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)

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
                    return redirect('mainpage:index')
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
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('change_password')
            else:
                return render(request, 'login/check.html', {'form': form})
        else:
            return render(request, 'login/check.html', {'form': form})

def password_edit_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'login/change_password.html')
        else:
            return render(request, 'mainpage/index.html')

    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return render(request, 'mainpage/index.html')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'login/change_password.html', {'password_change_form':password_change_form})

def blocked_view(request):
    return render(request, 'login/login_blocked.html')