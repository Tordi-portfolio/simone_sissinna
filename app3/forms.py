from django import forms
from .models import FanCard
from django.contrib.auth.models import User

class FanCardForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Assign to User",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = FanCard
        exclude = ['issued_on', 'created_at']
        widgets = {
            'valid_till': forms.DateInput(attrs={'type': 'date'}),
        }
