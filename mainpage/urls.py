from django.urls import path
from mainpage.views import Main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url path: /
    path('', Main.as_view()),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # img 저장 url