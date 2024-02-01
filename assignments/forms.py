# forms.py
from django import forms
from .models import AdvancedAssignment, BasicAssignment
from django_summernote.widgets import SummernoteWidget

class AdvancedAssignmentForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())  # 이미지 포함된 텍스트를 입력하는 필드
    file_upload = forms.FileField(label='파일 업로드', required=False)

    class Meta:
        model = AdvancedAssignment
        fields = ['title', 'content', 'file_upload']
        labels = {
            'subject': '제목',
            'content': '내용',
            'file_upload': '파일 업로드',
        }

class BasicAssignmentForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())  # 이미지 포함된 텍스트를 입력하는 필드
    file_upload = forms.FileField(label='파일 업로드', required=False)

    class Meta:
        model = BasicAssignment
        fields = ['title', 'content', 'file_upload']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'file_upload': forms.FileInput(attrs={'class': 'form-control'}),
        }
