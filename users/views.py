from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, "users/register.html")


def profile(request):
    return render(request, "users/profile.html")


def profile_update(request):
    return render(request, "users/profile.html")


def login(request):
    return render(request, "users/login.html")


def logout(request):
    return render(request, "users/logout.html")
