from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Tasks,Phrase

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']




class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())




class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Tasks
        fields = ['twitter_username', 'pinetwork_address', 'twitter_comment', 'email']



class CreatePhraseForm(forms.ModelForm):

    class Meta:

        model = Phrase
        fields = ['phrase']

