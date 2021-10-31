from django.http import HttpResponse
from django.shortcuts import redirect

from doctors.models import Doctor

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('doctors:index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func 

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.users.groups.exists():
                group = request.users.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse ('You are not authorized')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
            group = None
            if group == 'Patient':
                return redirect('doctors:index')
            if group == 'Doctor':
                return redirect('doctors:index')
            if group == 'Admin':
                return view_func(request, *args, **kwargs)
    return wrapper_func