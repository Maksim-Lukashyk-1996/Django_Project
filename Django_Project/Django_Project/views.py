from django.http import HttpResponse
from django.shortcuts import render

# Записал функцию
def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'home.html')







# def home(request):
#     return HttpResponse('This is my home')

# def about(request):
#     return HttpResponse('This is my first page')