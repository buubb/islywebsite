# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib import messages

class Login(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            messages.success(request, "어서오세요")
            return render(request, 'islyweb/index.html')
        else:
            return render(request, 'login/make.html')
            

    
    def post(self, request):
        print("post로 호출")
        if request.user.is_authenticated:
            messages.success(request, "어서오세요")
            return render(request, 'islyweb/index.html')
        else:
            return render(request, 'login/make.html')


class Logout(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            messages.add_message(request, messages.INFO, '로그아웃됩니다.')
            messages.info(request, "로그아웃됩니다.")
            Logout(request)
            return render(request, 'islyweb/index.html')



