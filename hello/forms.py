from django import forms


class HelloForm(forms.Form):
    name = forms.CharField(required=True)
    message = forms.CharField(required=True)