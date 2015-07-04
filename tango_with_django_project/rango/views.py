from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Rango says hey there world! <a href=\"/rango/about/\">about</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href=\"/rango/\">Homepage</a>")
