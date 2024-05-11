from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render

class CsrfFailureMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 403:
            # CSRF 토큰 검사 실패 시 메인 페이지로 리디렉션
            return render(request, 'mainpage/index.html')
        return response
