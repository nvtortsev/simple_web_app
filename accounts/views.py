from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm
from .models import User
from django.contrib.auth.models import auth
from django.contrib import messages


# регистрация
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
                full_name=form.cleaned_data["full_name"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
            )
            user.save()
            return redirect("/accounts/sign_in/")
    else:
        form = SignUpForm()

    return render(request, "accounts/sign_up.html", {"form": form})


# авторизация
def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info("Проверьте логин или пароль")
                return redirect("/accounts/sign_in/")
    else:
        form = SignInForm()

    return render(request, "accounts/sign_in.html", {"form": form})


# выход из аккаунта
def log_out(request):
    auth.logout(request)
    return redirect("/")
