from django.shortcuts import render

from django.http import  HttpResponse

def index( request ):
    return HttpResponse("Rango says hey there partner"+"\n this is the about page:" + about())

def about( request ):
    return HttpResponse("Rango says here is the about page" + "\n return back to the index:" + index())
