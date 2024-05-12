from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
            raise ValidationError(
                "비밀번호는 최소 8자 이상, 영문자, 숫자, 특수 문자(@$!%*#?&)를 포함해야 합니다.",
                code='invalid_password',
            )

    def get_help_text(self):
        return "비밀번호는 최소 8자 이상, 영문자, 숫자, 특수 문자(@$!%*#?&)를 포함해야 합니다."
