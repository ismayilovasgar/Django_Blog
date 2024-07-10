from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from .models import Post

posts = [
    {
        "author": "ASGAR ISMAYILOV",
        "title": "Blog Post 1",
        "content": "This is my first blog post",
        "date_posted": "7th August, 2024",
    },
    {
        "author": "Destiny Franks",
        "title": "Blog Post 2",
        "content": "This is my second blog post",
        "date_posted": "14th August, 2024",
    },
]


# Create your views here.
@login_required(login_url="login")
def home(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/home.html", context)


@login_required(login_url="login")
def about(request):
    return render(request, "blog/about.html")
