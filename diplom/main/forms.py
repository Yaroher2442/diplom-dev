from django import forms
from django.contrib.auth import get_user_model
from .models import Clients, Cases

users = get_user_model().objects.all()


class Register(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               required="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             required="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required="")


class CasesAdd(forms.Form):
    OPTIONS_CLIENTS = tuple([(item.id, item.name) for item in Clients.objects.all()])
    OPTIONS_OWNRES = tuple([(item.id, item.username) for item in get_user_model().objects.all()])
    # client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required="")
    client = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=OPTIONS_CLIENTS)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required="")
    executor = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=OPTIONS_OWNRES)


class ClientAdd(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required="")
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                            required="")
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required="")


class TaskAdd(forms.Form):
    CASE_OPTIONS = tuple([(item.id, item.name) for item in Cases.objects.all()])
    case = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=CASE_OPTIONS)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required="")
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required="")


class FunnelAdd(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required="")
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required="")
