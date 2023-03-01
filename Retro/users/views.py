from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from users.forms import AuthenticationForm, RegistrationForm


def page_login(request):
    if request.method == 'GET' and request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:home'))

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if "@" in username_or_email:  # We insist on that username can't contain '@' char
                user = authenticate(email=username_or_email, password=password)
            else:
                user = authenticate(username=username_or_email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Welcome!")
                return HttpResponseRedirect(reverse('users:profile'))
            messages.error(request, 'Incorrect username/email or password')
        else:
            messages.error(request, 'Incorrect form data')
    else:
        form = AuthenticationForm()

    context = {
        'title': 'Sign In',
        'form': form,
    }
    return render(request, 'users/signin.html', context)


def page_registration(request):
    if request.method == 'GET' and request.user.is_authenticated:
        messages.get_messages(request)
        return HttpResponseRedirect(reverse('main:home'))

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                messages.error(request, 'Passwords do not match')
            elif User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'This username is already registered')
            else:
                User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                )
                messages.success(request, 'Registration was successful!')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.error(request, 'Something went wrong. Please check if data is correct')
    else:
        form = RegistrationForm()

    context = {
        'title': 'Sign Up',
        'form': form,
    }
    return render(request, 'users/signup.html', context)


def page_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('main:home')))


@login_required(login_url='users:login')
def page_profile(request):
    context = {
        'title': request.user.username,
        'user': request.user,
    }
    return render(request, 'users/profile.html', context)
