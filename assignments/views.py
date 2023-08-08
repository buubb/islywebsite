# backend
from django.shortcuts import render
from rest_framework.views import APIView

from .models import BasicAssignment, AdvancedAssignment


def basic(request):
    return render(request, 'assignments/tem2.html')

def blog(request) :
    postlist = BasicAssignment.objects.all()
    return render(request, 'assignments/tem2.html',{'postlist':postlist})

#tem2.html -> basiclist.html
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

