from django.shortcuts import render, redirect
from .forms import loginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import LoginView
# Create your views here.


def mylogin(response):
    if response.user.is_authenticated:
        return redirect('../timeline')
    elif response.method == 'POST':
        form = loginForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                if 'next' in response.POST:
                    return redirect(response.POST.get('next'))
                else:
                    return redirect('../timeline')
            else:
                messages.warning(response, 'invalid Username or Password')
                return redirect('../login')
    else:
        form = loginForm()
    return render(response, 'login/login.html', {'form': form})
