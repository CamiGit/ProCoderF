from django import forms

class OrdersForms(forms.Form):
    number_order = forms.IntegerField()
    products = forms.__dict__
    time = forms.DateTimeField()