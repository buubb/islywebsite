# backend
from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'islyweb/index.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'islyweb/index.html')