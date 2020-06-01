from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangePicForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from codele.settings import dotenv_file
import requests
import os
import dotenv

def register(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        context = {
        'form':form
        }

        if form.is_valid():
            try:
                validate_recaptcha()
                form.save()
                return redirect('codele-registration-success')
            except:
                context['captcha'] = 'invalid'

        return render(request, 'users/register.html', context)
    else:
        return redirect('codele-profile-w')

def validate_recaptcha():
    dotenv.load_dotenv(dotenv_file)
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': os.getenv('CAPTCHA_SECRET'),
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()
    if result['sucess']:
        return True
    else:
        return False

def account_created(request):
        return render(request, 'users/success.html')

def profile(request, user_name):
    user = User.objects.filter(username=f'{user_name}').first()

    if request.method == 'POST':
        form = ChangePicForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            print(request.FILES)
            if 'picture' in request.FILES:
                profile.image = request.FILES['picture']

            profile.save()

    context = {
        'badge' : user.profile.badge,
        'profile_pic': user.profile.image.url,
        'username': user.username,
        'date_joined': user.date_joined,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email' : user.email,
        'lessons_completed': user.profile.lessons_completed,
        'user_banned': user.profile.banned
    }

    return render(request, 'users/profile.html', context)

@login_required
def profile_w(request):
        return profile(request, request.user.username)
