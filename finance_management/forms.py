from django import forms
from django.utils import timezone

class AddAccount(forms.Form):
    name = forms.CharField(max_length=128)
    balance = forms.DecimalField()
    currency = forms.CharField(max_length=4)

class AddTransaction(forms.Form):
    timestamp = forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now())
    accountID = forms.IntegerField()
    type = forms.CharField(max_length=8)
    amount = forms.DecimalField()
    remark = forms.CharField(max_length=256)