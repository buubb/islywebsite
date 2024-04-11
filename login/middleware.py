from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class KickedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        kicked = request.session.pop('kicked', None)
        if kicked:
            # 로그인된 사용자인 경우에만 메시지를 전달하고 로그아웃합니다. 
            # 로그인 페이지로 이동합니다.
            messages.debug(request, '동일 아이디로 다른 브라우저 웹사이트에서 로그인이 감지되어, 강제 로그아웃되었습니다.')
            auth_logout(request)
            login_url = '/'  # 로그인 페이지의 URL로 변경하세요
            return redirect(login_url)
