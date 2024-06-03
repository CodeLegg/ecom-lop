# forms.py

from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Full Name"}),
        required=True,
    )
    shipping_address1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Address 1"}),
        required=True,
    )
    shipping_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Address 2"}),
        required=False,
    )
    shipping_city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "City"}),
        required=True,
    )
    shipping_state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "State"}),
        required=False,
    )
    shipping_zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Zipcode"}),
        required=False,
    )
    shipping_country = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Country"}),
        required=True,
    )

    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_full_name',
            'shipping_address1',
            'shipping_address2',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode',
            'shipping_country',
        ]
