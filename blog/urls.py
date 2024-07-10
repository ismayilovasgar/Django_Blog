from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    # ? Function View
    # path("", views.home, name="blog-home"),
    path("about/", about, name="blog-about"),
    #
    #
    # ? Class View
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog-detail"),
    path("post/new", PostCreateView.as_view(), name="blog-new"),
]
