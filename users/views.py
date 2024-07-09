from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from users.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account Successfully Created for {username} Login In Now !!!"
            )
            return redirect("login")

    context = {"form": form}

    return render(request, "users/register.html", context)


@login_required(login_url="login")
def profile(request):
    # if request.method == "POST":
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(
    #         request.POST, request.FILES, instance=request.user.profile
    #     )

    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f"Your Profile was Updated !")
    #         return redirect("profile")

    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)

    # context = {
    #     "u_form": u_form,
    #     "p_form": p_form,
    # }
    return render(request, "users/profile.html")


@login_required(login_url="login")
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Profile was Updated !")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "users/profile_update.html", context)


@login_required(login_url="login")
def logout(request):
    return render(request, "users/logout.html")


def login(request):
    return render(request, "users/logout.html")
