# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Review


class RegistrationForm(UserCreationForm):

    username = forms.CharField(
        max_length=150,
        help_text="Required. Enter your username.",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your username", "class": "input-field"}
        ),
    )

    email = forms.EmailField(
        max_length=254,
        help_text="Required. Enter a valid email address.",
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email", "class": "input-field"}
        ),
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password", "class": "input-field"}
        ),
        help_text="Your password can't be too similar to your other personal information and must contain at least 8 characters.",
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm your password", "class": "input-field"}
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "This email is already associated with an existing account."
            )
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("The passwords do not match.")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your username", "class": "input-field"}
        ),
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password", "class": "input-field"}
        ),
    )



class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        # Insert <br> tag between fields
        self.fields['star_rating'].widget.attrs.update({'style': 'margin-bottom: 10px;'})
        
    class Meta:
        model = Review
        fields = ['star_rating', 'text']
        labels = {
            'text': 'Write Your Review',
        }
