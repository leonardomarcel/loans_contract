from django.contrib import auth as django_auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render



@login_required
def index(request):
    return render(request, 'index.html', locals())

def login(request):
    u"""."""
    user = request.user
    redirect_to = request.GET.get('next', '/')

    if user.id:
        return redirect('index')

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = django_auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_auth.login(request, user)
                return redirect(redirect_to)
            else:
                error_message = 'Usuário desativado.'
        else:
            error_message = 'Usuário e/ou senha inválido(s).'

    return render(request, 'login.html', locals())

@login_required
def logout(request,):
    u"""."""
    django_auth.logout(request)
    return redirect('login')


