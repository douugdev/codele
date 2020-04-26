from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    var = {
        'range' : list(range(5))
    }
    return  render(request, 'home/index.html', var)
