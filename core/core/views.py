from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def intro(request):
    return render(request, 'intro.html')