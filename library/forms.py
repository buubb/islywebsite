from django import forms
from .models import LibraryPost

class PostForm(forms.ModelForm):
    class Meta:
        model = LibraryPost
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content':'내용',
        }