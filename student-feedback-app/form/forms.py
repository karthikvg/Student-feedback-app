from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Login form
class LogInForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())

# Feedback Form
class FeedbackForm(forms.Form):
    title=forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Please give relevant title'}))

    feed_back=forms.CharField(
        max_length=500,
        required=True,

        widget=forms.Textarea(attrs={'rows':10,'class':'form-control','placeholder':'Enter your feedback!'}))


# Student registration form
class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Enter FirstName'}), )

    last_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Enter LastName'}), )

    middle_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Enter UserName'}), )

    roll_no=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'enter RollNumber'}),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-group', 'placeholder': 'Enter Password'}),
    )

    email_id=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'enter RollNumber'}),
    )
    picture=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'enter RollNumber'}),
    )

