from django import forms
from .models import Item

class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "item_desc", "item_price", "item_img"]
        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control text-light",
                "placeholder": "Enter the item name",
            }),
            'desc': forms.Textarea(attrs={
                "class": "form-control text-light",
                "placeholder": "Enter a description",
                "rows": 4,
            }),
            'price': forms.NumberInput(attrs={
                "class": "form-control text-light",
                "placeholder": "0.00",
            }),
            'image_url': forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Enter image URL or leave default",
                "value": "https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png",
            }),
        }

class SimpleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the item name",
        }),
        label="Item Name",
    )
    desc = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter a description",
            "rows": 4,
        }),
        label="Description",
        required=False,  # Optional field
    )
    price = forms.IntegerField(
        max_value=10000,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "0.00",
        }),
        label="Price (₹)",
        required=True
    )
    image_url = forms.URLField(
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "Enter image URL or leave default",
            "value": "https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png",
        }),
        label="Image URL",
        required=False,  # Optional field
    )