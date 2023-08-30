# backend
from django.shortcuts import render
from rest_framework.views import APIView
from volunteer.models import Post


class Volunteer(APIView):
    def get(self, request):
        print("get으로 호출")
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, 'volunteer/tem2.html', context)

    def post(self, request):
        print("post로 호출")
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, 'volunteer/tem2.html', context)

