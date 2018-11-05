from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm
from django.contrib.auth.models import User


def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/feed/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('loginsys/login.html', args)

    else:
        return render(request, 'loginsys/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password2'])
            auth.login(request, user)
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'loginsys/register.html', {'form': form})
