from django.shortcuts import redirect


class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.user.is_superuser and not request.user.is_staff and request.environ['PATH_INFO'].startswith('/admin/'):
            return redirect('/')
        return response