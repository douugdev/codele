from django.shortcuts import render
from .models import Question

def questions(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'questions/questions.html', context)

def question(request, question_id):
    pass
