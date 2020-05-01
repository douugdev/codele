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


def profile(request, user_name):

    user = User.objects.filter(username=f'{user_name}').first()
    context = {
        'badge' : user.profile.badge,
        'profile_pic': user.profile.image.url,
        'username': user.username,
        'date_joined': user.date_joined,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email' : user.email,
        'lessons_completed': user.profile.lessons_completed
    }

    return render(request, 'users/profile.html', context)


def profile_w(request):
    if request.user.is_authenticated:
        return profile(request, request.user.username)
    else:
        return redirect('codele-home')
