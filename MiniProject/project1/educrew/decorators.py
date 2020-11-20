from django.http import HttpResponse
from django.shortcuts import redirect

def user_authentication(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')
    return wrapper_func

def restricted_users(restricted_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group != "Admin":
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        return wrapper_func
    return decorator

def faculty_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Student':
            return redirect('home')
        if group == 'Faculty':
            return view_func(request, *args, **kwargs)
    return wrapper_func


def student_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Faculty':
            return redirect('home')
        if group == 'Student':
            return view_func(request, *args, **kwargs)
    return wrapper_func