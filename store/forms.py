# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.core.exceptions import ValidationError
from .models import Review
import re


class ChangePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your new password", "class": "input-field"}
        ),
        help_text=(
            "Your password can't be too similar to your other personal information, "
            "must contain at least 8 characters, "
            "and must contain at least one capital letter and one number."
        ),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm your new password", "class": "input-field"}
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get("new_password1")
        if len(new_password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", new_password1):
            raise ValidationError("Password must contain at least\none capital letter.")
        if not re.search(r"[0-9]", new_password1):
            raise ValidationError("Password must contain at least one number.")
        return new_password1

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError("The passwords do not match.")
        return new_password2


class UpdateUserForm(UserChangeForm):
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

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if (
            User.objects.filter(username__iexact=username)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise ValidationError("This username is already taken.")
        return username.lower()  # Convert username to lowercase

    def clean_email(self):
        email = self.cleaned_data["email"]
        if (
            User.objects.filter(email__iexact=email)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise ValidationError(
                "This email is already associated with an existing account."
            )
        return email


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
        help_text=(
            "Your password can't be too similar to your other personal information, "
            "must contain at least 8 characters, "
            "and must contain at least one capital letter and one number."
        ),
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
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("This username is already taken.")
        return username.lower()  # Convert username to lowercase

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(
                "This email is already associated with\nan existing account."
            )
        return email.lower()  # Convert email to lowercase

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password1):
            raise ValidationError("Password must contain at least\none capital letter.")
        if not re.search(r"[0-9]", password1):
            raise ValidationError("Password must contain at least one number.")
        return password1

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

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            # Check if the username exists in a case-insensitive manner
            user = User.objects.filter(username__iexact=username).first()
            if user is not None and user.check_password(password):
                self.user_cache = user
            else:
                raise forms.ValidationError("Username or password is incorrect.")

        return cleaned_data


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs["class"] = "mobile-textarea"

        # Insert <br> tag between fields
        self.fields["star_rating"].widget.attrs.update(
            {"style": "margin-bottom: 10px;"}
        )

    class Meta:
        model = Review
        fields = ["star_rating", "text"]
        labels = {
            "text": "Write Your Review",
        }


class EditReviewForm(ReviewForm):
    class Meta(ReviewForm.Meta):
        fields = ["star_rating", "text"]
        labels = {
            "text": "Re-write Your Review",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a custom CSS class to the textarea widget
        self.fields["text"].widget.attrs["class"] = "mobile-textarea"


class DeleteReviewForm(forms.Form):
    confirm_delete = forms.BooleanField(label="Confirm deletion")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["confirm_delete"].required = True

    def clean(self):
        cleaned_data = super().clean()
        confirm_delete = cleaned_data.get("confirm_delete")
        if not confirm_delete:
            raise forms.ValidationError(
                "Please confirm deletion by checking the checkbox."
            )
