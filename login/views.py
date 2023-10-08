# backend
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class Login(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            return render(request, 'islyweb/index.html')
        else:
            return render(request, 'login/make.html')
            return redirect('login:make')

    
    def post(self, request):
        print("post로 호출")
        if request.user.is_authenticated:
            return render(request, 'islyweb/index.html')
        else:
            return render(request, 'login/make.html')


class Logout(APIView):
    def get(self, request):
        print("get으로 호출")
        if request.user.is_authenticated:
            Logout(request)
            return render(request, 'islyweb/index.html')



