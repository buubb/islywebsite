from django.contrib import admin

from .models import BasicAssignment, AdvancedAssignment

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능

admin.site.register(BasicAssignment)
admin.site.register(AdvancedAssignment)