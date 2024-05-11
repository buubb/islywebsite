# forms.py
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    profile_image = forms.ImageField(label="프로필 이미지", required=False)

    class Meta:
        model = Comment
        fields = [
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
