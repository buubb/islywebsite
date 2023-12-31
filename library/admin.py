from django.contrib import admin

from .models import LibraryPost, LibraryComment

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(LibraryPost)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['post']
admin.site.register(LibraryComment)