from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangePicForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        if form.is_valid():

            form.save()

            return redirect('codele-registration-success')

        return render(request, 'users/register.html', {'form':form})
    else:
        return redirect('codele-profile-w')


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
