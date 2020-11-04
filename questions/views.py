from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.models import User

def questions(request):

    #Search query yay
    query = request.GET.get("query")

    if query:
        #Checks if query exists then search for it in the questions
        #stored in the database, looking for matching titles.
        queryset_list = Question.objects.filter(title__icontains=query)
        for item in Question.languages:
            if query.upper() in item:
                queryset_list = Question.objects.filter(language__icontains=item[0])

            #This conditional looks confusing, it checks if the
            #user made an input of a language (e.g: JS or PY) instead of a
            #question title, then display all questions related to that
            #specific language.
            elif query.capitalize() in list(map(lambda x: str(x).capitalize(), item)):
                queryset_list = Question.objects.filter(language__icontains=item[0])
    else:
        queryset_list = Question.objects.all()
    context = {
        #Ugly way of showing the most recent questions.
        'questions': queryset_list[::-1]
    }
    return render(request, 'questions/questions.html', context)

def question(request, question_id):
    '''
    This function renders a specific question and its answers.
    '''

    qt = Question.objects.filter(id__icontains=question_id).first()
    user = User.objects.filter(username=qt.author).first()
    answers = Answer.objects.filter(question=qt)
    answersauthors = []

    for answer in answers:
        answersauthors.append(User.objects.filter(username=answer.author).first().username)

    context = {
        'id' : qt.id,
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
    '''
    Render function for the question creation view. It contains
    a form that contacts a database model in models.py
    '''

    if request.user.is_authenticated:
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('codele-questions')
        return render(request, 'questions/create_question.html')
    else:
        return redirect('codele-home')

def answer(request, question_id):
    if request.user.is_authenticated:
        form = AnswerForm(request.POST or None)
        context = {
            'questionid' : question_id,
            'qt' : Question.objects.filter(id__icontains=question_id).first()
        }

        if form.is_valid():
            form.save()
            return redirect('codele-question', question_id)
            
        elif form.errors:
            print(f'{form.fields}\n{form.errors}')
        return render(request, 'questions/answer.html', context)
    else:
        return redirect('codele-home')
