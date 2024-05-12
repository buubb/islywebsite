from django.contrib.auth.hashers import check_password
from django import forms
from .models import BoardMember

class LoginForm(forms.Form):
    # 입력받을 값 두개
    username = forms.CharField(error_messages={
        'required':'아이디를 입력하세요!'
    },max_length=100, label="사용자이름")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="password")
    # 처음 값이 들어왔다 는 검증 진행
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            member = BoardMember.objects.filter(username=username).first()

            if not member or not check_password(password, member.password):
                self.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다!')
