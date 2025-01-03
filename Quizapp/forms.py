from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegisterFrom(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email-address",
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password"}
        ),
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confim password"}
        ),
        help_text=None,
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email-address",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password"}
        ),
    )
