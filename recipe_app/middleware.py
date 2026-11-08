from django.contrib.auth import login
from django.contrib.auth.models import User


class AdminNoPasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin'):
            if not request.user.is_authenticated or not request.user.is_staff:
                admin_user = User.objects.filter(is_superuser=True).first()
                if not admin_user:
                    admin_user = User.objects.create_superuser('admin', 'admin@example.com', '')
                login(request, admin_user, backend='django.contrib.auth.backends.ModelBackend')
        return self.get_response(request)
