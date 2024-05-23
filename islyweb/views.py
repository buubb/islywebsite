# backend
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseNotFound, HttpResponseServerError
    
# 400 Error
def bad_request(request, exception):
    return render(request, 'error/404page.html', status=400)

# 404 Error
def page_not_found(request, exception):
    return render(request, 'error/404page.html')

# 500 Error
def server_error(request):
    return render(request, 'error/500page.html', status=500)

