from django import forms
from .models import LibraryPost, LibraryComment

class PostForm(forms.ModelForm):
    class Meta:
        model = LibraryPost
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content':'내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = LibraryComment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }