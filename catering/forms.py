from django import forms
from .models import Catering

class CateringForm(forms.ModelForm):
    class Meta:
        model = Catering
        fields = ['food_item', 'drink_item', 'food_quantity', 'drink_quantity']
