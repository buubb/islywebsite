# forms.py
from django import forms
from .models import AdvancedAssignment, BasicAssignment

class AdvancedAssignmentForm(forms.ModelForm):
    class Meta:
        model = AdvancedAssignment
        fields = ['title', 'content', 'file_upload']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'file_upload': forms.FileInput(attrs={'class': 'form-control'}),
        }

class BasicAssignmentForm(forms.ModelForm):
    class Meta:
        model = BasicAssignment
        fields = ['title', 'content', 'file_upload']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'file_upload': forms.FileInput(attrs={'class': 'form-control'}),
        }
