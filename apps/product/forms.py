from django import forms
from .models import Product


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()
