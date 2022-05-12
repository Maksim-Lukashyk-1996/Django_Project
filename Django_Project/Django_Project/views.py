from django.http import HttpResponse
from django.shortcuts import render

# Записал функцию
def about(request):
    return render(request, 'about.html')
def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render(request, 'reverse.html', {'word':reverse})
def home(request):
    return render(request, 'home.html')







# def home(request):
#     return HttpResponse('This is my home')

# def about(request):
#     return HttpResponse('This is my first page')