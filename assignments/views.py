from django.shortcuts import render
from rest_framework.views import APIView

class BasicList(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/basiclist.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/basiclist.html')
    
class AdvancedList(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/advancedlist.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/advancedlist.html')

class Submit(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/submit.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/submit.html')