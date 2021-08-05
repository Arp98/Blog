from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForms
from .models import Account
from django.contrib.auth import authenticate, login as auth_login
import datetime


def Login(request):
    if request.user.is_authenticated:
        return redirect('/Dashboard/NewPost')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    users = Account.objects.get(username=username)
                    users.login_count = int(users.login_count) + 1
                    users.login_time = datetime.datetime.now()
                    users.save()
                    return redirect('/Dashboard/NewPost')
                else:
                    messages.info(request, 'your account has been disabled \n Please login again')
                    return render(request, 'Login.html')
            else:
                messages.info(request, 'Invalid Credentials')
                return render(request, 'Login.html')
        else:
            return render(request, 'Login.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/Dashboard/NewPost')
    else:
        if request.method == 'POST':
            form = CreateUserForms(request.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                form.save()
                account = authenticate(username=username, password=raw_password)
                auth_login(request, account, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'Account Successfully created for ' + username)
                return redirect('/Account/Login')
            else:
                return render(request, 'SignUp.html', {'form': form})

        else:
            form = CreateUserForms()
            return render(request, 'SignUp.html', {'form': form})
