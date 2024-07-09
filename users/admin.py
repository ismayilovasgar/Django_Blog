from django.contrib import admin
from users.models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
    list_filter = ["user"]

    class Meta:
        model = Profile


# admin.site.register(Profile,ProfileAdmin)
