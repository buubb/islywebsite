# forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _

class UserChangePasswordForm(PasswordChangeForm):
    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get('new_password1')
        
        # 여기에 추가적인 유효성 검사를 수행할 수 있습니다.
        # 예를 들어, 새 비밀번호의 길이가 8자 미만일 경우 오류를 발생시킵니다.
        if len(new_password1) < 8:
            raise forms.ValidationError(_("Your password must contain at least 8 characters."))
        
        return new_password1
