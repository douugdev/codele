from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():

        form.save()

        return redirect('codele-registration-success')

    return render(request, 'users/register.html', {'form':form})

def account_created(request):
        return render(request, 'users/success.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        return redirect('codele-home')
