from django import forms
from django.contrib.auth import get_user_model
from .models import Clients

users = get_user_model().objects.all()


class Register(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               required="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             required="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required="")


class CasesAdd(forms.Form):
    OPTIONS_CLIENTS = tuple([(item.name, item.id) for item in Clients.objects.all()])
    OPTIONS_OWNRES = tuple([(item.username, item.id) for item in get_user_model().objects.all()])
    # client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    client = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=OPTIONS_OWNRES)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required="")
    executor = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=OPTIONS_OWNRES)
