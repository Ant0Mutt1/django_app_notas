from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class':'form-control'
        }))
    username = forms.CharField(label='Nombre de Usuario', max_length=100, min_length=5, widget=forms.TextInput(attrs={
        'class':'form-control'
        }))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    password2 = forms.CharField(label='Confirmación contraseña', widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    
    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError('El usuario ya existe')
        return username
    
    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError('La dirección de email ya existe ')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden')
        return password2
    def save(self, commit = True):
        user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'],
                                        self.cleaned_data['password2'])
        return user
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')