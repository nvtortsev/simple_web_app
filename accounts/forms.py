from django import forms
from .models import User
from django.core.exceptions import ValidationError


# валидация фио
def validate_full_name(value):
    pass


# валидация номера телефона
def validate_phone(value):
    pass


class SignUpForm(forms.Form):
    username = forms.CharField(label="Логин", min_length=4)
    password = forms.CharField(label="Пароль", min_length=4, widget=forms.PasswordInput)
    full_name = forms.CharField(
        label="ФИО", max_length=100, validators=[validate_full_name]
    )
    phone = forms.CharField(label="Номер телефона", validators=[validate_phone])
    email = forms.EmailField(label="Email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("Такой логин уже используется")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот email уже используется")
        return email


class SignInForm(forms.Form):
    username = forms.CharField(label="Логин", min_length=4)
    password = forms.CharField(label="Пароль", min_length=4, widget=forms.PasswordInput)
