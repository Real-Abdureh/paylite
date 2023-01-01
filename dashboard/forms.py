from django import forms
from .models import Transaction



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['select', 'Payer_Name', 'Payer_Phone_no', 'Payer_Email', 'Service', 'Amount']

