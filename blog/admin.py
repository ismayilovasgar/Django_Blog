from django.contrib import admin
from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title"]
    list_display_links = ["author"]
    search_fields = ["auhtor", "title", "content"]
    list_filter = ["date_posted", "title"]

    class Meta:
        model = Post


# old way
# admin.site.register(Post, PostAdmin)
