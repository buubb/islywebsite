from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "팀 회고 작성하기...",
                }
            )
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "year",
            "generation",
            "content",
        ]