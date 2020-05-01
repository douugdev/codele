from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if not request.user.profile.banned:
            return render(request, 'home/index.html')
        else:
            logout(request)
            return render(request, 'home/banned.html')
    else:
        return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')
