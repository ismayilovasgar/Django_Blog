from django.contrib import admin
from django.urls import path, include
from blog.views import *
from users import views as users_views
from django.contrib.auth.views import LogoutView, LoginView
from blog import views

# For Image --------------------------------------------
from django.conf import settings
from django.conf.urls.static import static
# -------------------------------------------------------
urlpatterns = [

    path("", include("blog.urls")),
    path("admin/", admin.site.urls),
    #
    # user authentications
    path("register/", users_views.register, name="register"),
    path("profile/", users_views.profile, name="profile"),
    path("profile/profile_update/", users_views.profile_update, name="profile-update"),
    path("login/",LoginView.as_view(template_name="users/login.html", next_page="profile"),name="login",),
    path("logout/",LogoutView.as_view(template_name="users/logout.html"),name="logout",),

]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
