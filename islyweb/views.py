# backend
from django.shortcuts import render
from rest_framework.views import APIView
from django.template import RequestContext
from django.http import HttpResponseNotFound, HttpResponseServerError

class Main(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'islyweb/index.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'islyweb/index.html')
    
# 400 Error
def bad_request(request, exception):
    return render(request, '404page.html', status=400)

# 404 Error
def page_not_found(request, exception):
    return render(request, '404page.html')

# 500 Error
def server_error(request):
    return render(request, '404page.html', status=500)

