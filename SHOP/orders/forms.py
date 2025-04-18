from django import forms

class CouponForm(forms.Form):
    code = forms.CharField(label='', widget=forms.TextInput(attrs={
    'type' : "text",
    'name' : "count",
    'class' :"counter",
    }))