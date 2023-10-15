from django import forms
from .models import LibraryPost, LibraryComment
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())  # 이미지 포함된 텍스트를 입력하는 필드
    library_file_upload = forms.FileField(label='파일 업로드', required=False)
    
    class Meta:
        model = LibraryPost
        fields = ['subject', 'content', 'library_file_upload']
        labels = {
            'subject': '제목',
            'content':'내용',
            'file_upload': '파일 업로드',
        }
        
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = LibraryComment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }