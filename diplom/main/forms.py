from django import forms
from django.contrib.auth import get_user_model
from .models import Clients, Cases


class Register(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True)


class CasesAdd(forms.Form):
    OPTIONS_CLIENTS = tuple([(item.id, item.name) for item in Clients.objects.all()])
    OPTIONS_OWNRES = tuple([(item.id, item.username) for item in get_user_model().objects.all()])
    # client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    client = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=OPTIONS_CLIENTS)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)
    executor = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=OPTIONS_OWNRES)


class ClientAdd(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                            required=True)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)


class TaskAdd(forms.Form):
    CASE_OPTIONS = tuple([(item.id, item.name) for item in Cases.objects.all()])
    case = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
        choices=CASE_OPTIONS)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}),
                            required=True)


class FunnelAdd(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)
