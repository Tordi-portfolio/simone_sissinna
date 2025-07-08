from django import forms
from .models import FanCard

class FanCardForm(forms.ModelForm):
    class Meta:
        model = FanCard
        exclude = ['user', 'issued_on', 'created_at']
        widgets = {
            'valid_till': forms.DateInput(attrs={'type': 'date'}),
        }
