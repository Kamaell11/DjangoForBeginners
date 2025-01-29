from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Witaj w naszym sklepie!</h1><p>To strona główna.</p>")
