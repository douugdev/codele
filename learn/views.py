from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import re

@login_required
def welcome(request):
    user = User.objects.filter(username__icontains=request.user).first()

    #This conditional just checks if it's the user's first access
    if user.profile.last_lesson != 'None':
        last_lesson_language, last_lesson_id = user.profile.last_lesson.split(',')
    else:
        last_lesson_language, last_lesson_id = 'None', 'None'

    context = {
        "last_lesson_id": last_lesson_id,
        "last_lesson_language": last_lesson_language,
        "last_lesson": user.profile.last_lesson,
        "first_name": user.first_name.capitalize()
    }
    
    return render(request, 'learn/welcome.html', context)

@login_required
def learn(request, language):
    return render(request, f'learn/{str(language)}/index.html')

@login_required
def lesson(request, language, lesson_id):
    languages = ['python', 'java', 'gml', 'javascript']
    regex = re.compile('^[0-9]*$', re.I)

    user = User.objects.filter(username__icontains=request.user).first().profile
    if (language in languages) and (regex.match(lesson_id)):
        user.last_lesson = f'{language},{lesson_id}'
        user.save()
        return render(request, f'learn/{str(language)}/lessons/{str(lesson_id)}.html')
    else:
        return redirect('codele-welcome')
