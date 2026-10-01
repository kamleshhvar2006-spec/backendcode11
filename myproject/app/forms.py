from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "What needs to be done?", "autofocus": True}),
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "Details (optional)"}),
        }
