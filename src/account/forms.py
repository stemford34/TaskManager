from django import forms

from .models import User


class LoginForm(forms.Form):
    email       = forms.EmailField(label='email', required=False)
    password    = forms.CharField(label='password',  widget=forms.PasswordInput, required=False)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)
        


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',) #'full_name',)