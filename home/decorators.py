from django.http import HttpResponse
from django.shortcuts import redirect


# stops authenticated user for viewing the login and register pages
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # if user is authenticated stay on the dashboard else user must log in
        if request.user.is_authenticated:
            # dashboard
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


# which user see a page
def allowed_users(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            # check if user is part of a group
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            # check if group is in the role
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # don not allow the user
                return HttpResponse("You are not authorized ")
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'freelancer' or group == 'jobOwner':
            return redirect('user')

        if group == 'adminside':
            return view_func(request, *args, **kwargs)

    return wrapper_func
