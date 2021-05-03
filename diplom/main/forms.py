from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from .models import Clients, Cases


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class MyModelChoiceField_2(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username


class Register(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True)


class CasesAdd(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    client = MyModelChoiceField(queryset=Clients.objects.all(),
                                widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_client'}),
                                to_field_name="id", label="name", empty_label=None)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)
    executor = MyModelChoiceField_2(queryset=get_user_model().objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_client'}),
                                    to_field_name="id", label="name", empty_label=None)


class ClientAdd(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                            required=True)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)


class TaskAdd(forms.Form):
    OPTIONS = (
        ("Created", "Created"),
        ("Wait", "Wait"),
        ("Canceled", "Canceled"),
        ("Done", "Done"),
        ("Stop", "Stop")
    )
    case = MyModelChoiceField(queryset=Cases.objects.all(),
                              widget=forms.Select(attrs={'class': 'form-control', 'id': 'selector_owner'}),
                              to_field_name="id", label="name", empty_label=None)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)
    status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                               choices=OPTIONS)


class FunnelAdd(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                           required=True)
    descr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                            required=True)
