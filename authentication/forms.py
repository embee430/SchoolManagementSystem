# authentication/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Child

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('1', 'Admin'),
        ('2', 'Teacher'),
        ('3', 'Student'),
    ]
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'date_of_birth', 'parent_name', 'contact_number', 'address', 'passport_image', 'gender']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'gender': forms.Select(choices=Child.GENDER_CHOICES),
        }