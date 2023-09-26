from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content':'내용',
        }