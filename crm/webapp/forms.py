from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

from django import forms

class createuserform(UserCreationForm):

    class meta:

        model = User
        fields = ['username', 'password1', 'password2']



        class loginform(AuthenticationForm):
            


username = forms.CharField(widget=TextInput())
password = forms.CharField(widget=passwordinput())