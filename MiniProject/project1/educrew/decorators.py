from django.http import HttpResponse
from django.shortcuts import redirect

def user_authentication(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')
    return wrapper_func