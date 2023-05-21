from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1', 'address_line_2', 'country', 'state', 'city', 'order_note']

        def clean_email(self):
            data = self.cleaned_data['email']
        
            # Check for the condition that should raise an error
            if data != 'expected_value':
                raise forms.ValidationError('Invalid value for email')

            return data