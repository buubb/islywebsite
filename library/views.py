# backend
from django.shortcuts import render
from rest_framework.views import APIView


class Library(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'library/tem2.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'library/tem2.html')
    
class Library_Write(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'library/library_write.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'library/library_write.html')

  