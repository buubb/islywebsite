from django.urls import path
from mainpage.views import Main
from django.conf import settings
from django.conf.urls.static import static
from .views import get_instagram_token,refresh_instragram_token

urlpatterns = [
    # url path: /
    path('', Main.as_view()),
    path('get-instagram-token/', get_instagram_token, name='get_instagram_token'),
    path('refresh-instagram-token/', refresh_instragram_token, name='refresh_instagram_token'),

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # img 저장 url