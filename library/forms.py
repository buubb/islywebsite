from django import forms
from .models import LibraryPost, LibraryComment
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())  # 이미지 포함된 텍스트를 입력하는 필드

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