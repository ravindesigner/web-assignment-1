from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Welcome to my Website, I'm Ravin Awder!")