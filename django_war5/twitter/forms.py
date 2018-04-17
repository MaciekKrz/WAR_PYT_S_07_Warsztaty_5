from django import forms
from .models import Tweet


class TweetModelForms(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'


class AddUserForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)
    first_name = forms.CharField(label='name')
    last_name = forms.CharField(label='last_name')
    email = forms.EmailField(label='email')


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=64, strip=True)
    password = forms.CharField(label='password', max_length=64, widget=forms.PasswordInput)

