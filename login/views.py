# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

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
                login(request, user)
            return render(request, 'islyweb/index.html')
        else:
            return render(request, 'login/make.html')


class Logout(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            Logout(request)
        return render(request, 'islyweb/index.html')



