# backend
from django.shortcuts import render
from rest_framework.views import APIView

class BasicList(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/tem2.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/tem2.html')
    
class AdvancedList(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/tem3.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/tem3.html')

class Submit(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/tem4.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/tem4.html')