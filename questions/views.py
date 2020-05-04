from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm
from django.contrib.auth.models import User

def questions(request):
    query = request.GET.get("query")
    if query:
        queryset_list = Question.objects.filter(title__icontains=query)
        for item in Question.languages:
            if query.upper() in item:
                queryset_list = Question.objects.filter(language__icontains=item[0])
            elif query.capitalize() in list(map(lambda x: str(x).capitalize(),item)):
                queryset_list = Question.objects.filter(language__icontains=item[0])
    else:
        queryset_list = Question.objects.all()
    context = {
        'questions': queryset_list[::-1]
    }
    return render(request, 'questions/questions.html', context)

def question(request, question_id):
    qt = Question.objects.filter(id__icontains=question_id).first()
    user = User.objects.filter(username=qt.author).first()
    answers = Answer.objects.filter(question=qt)
    answersauthors = []
    for answer in answers:
        answersauthors.append(User.objects.filter(username=answer.author).first().username)

    context = {
        'title': qt.title,
        'author': user,
        'question': qt.question,
        'lang': qt.language,
        'authorpic': user.profile.image.url,
        'answers': answers,
        'answersauthors': answersauthors
    }
    return render(request, 'questions/question.html', context)

def create_question(request):
    if request.user.is_authenticated:
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('codele-questions')
        return render(request, 'questions/create_question.html')
    else:
        return redirect('codele-home')
