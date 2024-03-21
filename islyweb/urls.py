"""
URL configuration for islyweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Main
# all url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view()),
    path('notice/', include('notice.urls')),
    path('assignments/', include('assignments.urls')),
    path('login/', include('login.urls')),
    path('introduction/', include('introduction.urls')),
    path('library/', include('library.urls')),
    path('team-activities/', include('team_activities.urls')),
    path('volunteer/', include('volunteer.urls')),
    path('CTF-Challenge/', include('CTF_Challenge.urls')),
    path('recruit/', include('recruit.urls')),
    path('markdownx/', include('markdownx.urls')),  
]

#summernote 설정
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [path('summernote/', include('django_summernote.urls'))]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    