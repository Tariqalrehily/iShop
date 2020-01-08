from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='CVV', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=[(i, i) for i in range(1, 12)], required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=[(i, i) for i in range(2020, 2037)], required=False)
    # input hiden from the user
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'state'
        )