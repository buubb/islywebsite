#forms.py
from django import forms
from .models import TeamActivitiesPost

class TeamActivitiesForm(forms.ModelForm):
    class Meta:
        model = TeamActivitiesPost
        fields = ['title','content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }