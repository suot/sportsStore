from django import forms
from store.models import Order, Client, User
from django.utils.safestring import mark_safe

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['product', 'num_units']
        labels = {
            'num_units': mark_safe('<br/>Quantity'),
        }

class InterestForm(forms.Form):
    INTEREST_CHOICES = [
        (1, 'Yes'),
        (0, 'No')
    ]
    interested = forms.IntegerField(widget=forms.RadioSelect(choices=INTEREST_CHOICES))
    quantity = forms.IntegerField(min_value=1, initial=1)
    comments = forms.CharField(widget=forms.Textarea, label=mark_safe('<br/>Additional Comments'), required=False)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'avatar']
        labels = {
            'first_name': mark_safe('<br/>First name'),
            'email': mark_safe('<br/>Email address')
        }
        help_texts = {
            'username': None,
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
