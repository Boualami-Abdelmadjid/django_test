from django import forms
from main.models import Receipt
from django.contrib.auth.models import User


class ReceiptForm(forms.Form):
    store_name = forms.CharField()
    item_list = forms.CharField(widget=forms.Textarea)
    purchase_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD hh-mm-ss',"type":"datetime-local"}))
    total = forms.CharField()

    def save(self,user):
        Receipt.objects.create(user=user,**self.cleaned_data)

class RegistrationForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    password_2 = forms.CharField(widget=forms.PasswordInput(),required=True)

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
