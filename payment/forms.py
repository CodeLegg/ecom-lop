from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Full Name"}
        ),
        required=True,
    )
    shipping_address1 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Address 1"}
        ),
        required=True,
    )
    shipping_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Address 2"}
        ),
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
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Zipcode"}
        ),
        required=False,
    )
    shipping_country = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Country"}
        ),
        required=True,
    )

    class Meta:
        model = ShippingAddress
        fields = [
            "shipping_full_name",
            "shipping_address1",
            "shipping_address2",
            "shipping_city",
            "shipping_state",
            "shipping_zipcode",
            "shipping_country",
        ]


class PaymentForm(forms.Form):
    card_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Name On Card"}
        ),
        required=True,
    )
    card_number = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Card Number"}
        ),
        required=True,
    )
    card_exp_date = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Expiration Date"}
        ),
        required=True,
    )
    card_cvv_number = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "CVV Code"}
        ),
        required=True,
    )
    card_address1 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Billing Address 1"}
        ),
        required=True,
    )
    card_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Billing Address 2"}
        ),
        required=False,
    )
    card_city = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Billing City"}
        ),
        required=True,
    )
    card_state = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Billing County/State"}
        ),
        required=True,
    )
    card_zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Billing Postcode/Zipcode"}
        ),
        required=True,
    )
    card_country = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "input-field", "placeholder": "Billing Country"}
        ),
        required=True,
    )
