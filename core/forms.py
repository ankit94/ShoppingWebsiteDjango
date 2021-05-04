from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import Item, CATEGORY_CHOICES, LABEL_CHOICES


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)


class AddProductForm(forms.Form):
    title = forms.CharField(required=False)
    price = forms.FloatField(required=False)
    label = forms.ChoiceField(choices=LABEL_CHOICES)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=True)
    slug = forms.SlugField(required=False)
