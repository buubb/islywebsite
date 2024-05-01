# forms.py
from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "name",
            "point",
            "challenge",
            "dreamhack_link",
            "profile_image"
        ]
