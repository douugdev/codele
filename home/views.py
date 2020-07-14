from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def view_help(request):
    return render(request, 'home/help.html')
