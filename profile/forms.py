from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

class RegisterUserForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username','password1','password2','captcha')

        labels = {
            'username':'',
        }

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','type':'text','name':'username', 'placeholder':'Username'})
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password confirmation'