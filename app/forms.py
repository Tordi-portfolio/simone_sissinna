from django import forms
from django.contrib.auth.models import User
from .models import PrivateChat

# Message Form with File Support (Text, Image, Video)
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateChat
        fields = ['message', 'file']
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Type your message...',
                'rows': 2
            }),
        }

# User Registration Form
class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name'
    }))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
