from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request): #выполняет функцию, отправляет на страницу пассворд.хтмл

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12)) #задаем длину по значению length из формы

    if request.GET.get('uppercase'): #если включен параметр апперкейс, то расширяем список
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'): #если включен параметр спешл, то расширяем список
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'): #если включен параметр намберс, то расширяем список
        characters.extend(list('0123456789'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {"password" : thepassword})
