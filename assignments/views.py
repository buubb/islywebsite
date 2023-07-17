from django.shortcuts import render
from rest_framework.views import APIView

class AssignmentsList(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/list.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/list.html')
    
class AssignmentsSubmit(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'assignments/submit.html')
    
    def post(self, request):
        print("post로 호출")
        return render(request, 'assignments/submit.html')