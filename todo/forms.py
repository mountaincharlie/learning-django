# inorder to control and manage form functionality with Django
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:  # info about itself/how to render etc
        model = Item
        fields = ['name', 'done']
