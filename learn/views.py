from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def welcome(request):
    if not request.user.is_authenticated:
        return redirect(request, 'codele-register')

    user = User.objects.filter(username__icontains=request.user).first()

    if user.profile.last_lesson != 'None':
        last_lesson_language, last_lesson_id = user.profile.last_lesson.split(',')
        context = {
            "last_lesson_id": last_lesson_id,
            "last_lesson_language": last_lesson_language,
            "last_lesson": user.profile.last_lesson,
            "first_name": user.first_name.capitalize()
        }
    else:
        context = {
            "last_lesson_id": 'None',
            "last_lesson_language": 'None',
            "last_lesson": user.profile.last_lesson,
            "first_name": user.first_name.capitalize()
        }
    return render(request, 'learn/welcome.html', context)

def learn(request, language):
    if not request.user.is_authenticated:
        return redirect(request, 'codele-register')

    return render(request, f'learn/{str(language)}/index.html')

def lesson(request, language, lesson_id):
    if not request.user.is_authenticated:
        return redirect(request, 'codele-register')

    user = User.objects.filter(username__icontains=request.user).first().profile
    user.last_lesson = f'{language},{lesson_id}'
    user.save()

    return render(request, f'learn/{str(language)}/{str(lesson_id)}.html', context)
