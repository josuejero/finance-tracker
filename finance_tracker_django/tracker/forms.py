from django import forms

class PaymentForm(forms.Form):
    description = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    due_date = forms.DateField(widget=forms.SelectDateWidget)
    frequency = forms.CharField(max_length=50)

class TransactionForm(forms.Form):
    description = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    date = forms.DateField(widget=forms.SelectDateWidget)
