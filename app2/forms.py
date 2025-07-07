from django import forms
from .models import GalleryImage

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'caption']


from django import forms
from .models import FansCard

class FansCardForm(forms.ModelForm):
    class Meta:
        model = FansCard
        fields = ['name', 'card_type', 'price', 'quantity', 'description', 'image']


from django import forms
from .models import UserFanCardRecord

class AdminUploadFanCardForm(forms.ModelForm):
    class Meta:
        model = UserFanCardRecord
        fields = ['user', 'store_card', 'delivered_card_image', 'message', 'name', 'card_type', 'price', 'quantity']
