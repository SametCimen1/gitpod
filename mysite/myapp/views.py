from django.shortcuts import render

# Create your views here.
from django.urls import include,path
from django.http import HttpResponse

def index(req):
    return HttpResponse("Hello this is the index page")