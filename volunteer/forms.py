# forms.py
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "name",
            "content",
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "year",
            "generation",
            "content",
        ]
