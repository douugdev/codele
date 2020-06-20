from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def view_help(request):
    return render(request, 'home/help.html')
