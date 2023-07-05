from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return render(request,'recipe/home.html')

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return render(request,'recipe/contato.html')
