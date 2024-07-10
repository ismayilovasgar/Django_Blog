from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from .models import Post

# -------------------------------------------------------
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# -------------------------------------------------------

# posts = [
#     {
#         "author": "ASGAR ISMAYILOV",
#         "title": "Blog Post 1",
#         "content": "This is my first blog post",
#         "date_posted": "7th August, 2024",
#     },
#     {
#         "author": "Destiny Franks",
#         "title": "Blog Post 2",
#         "content": "This is my second blog post",
#         "date_posted": "14th August, 2024",
#     },
# ]

# ? Function View
# Create your views here.
# @login_required(login_url="login")
# def home(request):
#     context = {
#         "posts": Post.objects.all(),
#     }
#     return render(request, "blog/home.html", context)


@login_required(login_url="login")
def about(request):
    return render(request, "blog/about.html")


# ? Class View
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = "-date_posted"
    template_name = "blog/home.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ["title", "content"]

    success_url = reverse_lazy("blog-home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
