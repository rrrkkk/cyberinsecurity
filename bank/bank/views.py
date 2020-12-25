from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Al's Trustworthy Index.")

def bank(request):
    return HttpResponse("Hello, world. You're at the Al's Trustworthy Bank.")
