from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('codele-welcome')
    return render(request, 'home/index.html')

def view_help(request):
    return render(request, 'home/help.html')
