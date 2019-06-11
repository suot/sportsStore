from django import forms
from store.models import Order
from django.utils.safestring import mark_safe

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['product', 'num_units', 'client']
        widgets = {
            'client': forms.RadioSelect,
        }
        labels = {
            'num_units': mark_safe('<br/>Quantity'),
            'client': mark_safe('<br/>Client Name')
        }

class InterestForm(forms.Form):
    INTEREST_CHOICES = [
        (1, 'Yes'),
        (0, 'No')
    ]
    interested = forms.IntegerField(widget=forms.RadioSelect(choices=INTEREST_CHOICES))
    quantity = forms.IntegerField(min_value=1, initial=1)
    comments = forms.CharField(widget=forms.Textarea, label=mark_safe('<br/>Additional Comments'), required=False)
