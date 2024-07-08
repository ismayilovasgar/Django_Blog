from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome My home </h1>")


def about(request):
    return HttpResponse("<h1> Welcome My about </h1>")
