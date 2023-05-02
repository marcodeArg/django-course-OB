from django.forms import ModelForm
from django import forms
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'stock']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
