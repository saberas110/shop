from django import forms
from .models import AvailableColor


class ProductForm(forms.Form):
    def __iter__(self):
        for obj in AvailableColor.objects.all():
            color1 = forms.ChoiceField(label='ioi', widget=forms.CheckboxInput(attrs={
                'autocomplete': "off",
                'class': "btn-check",
                'id': f'{obj.color.name}',
                'name': f'{obj.color.name}',
                'type': "radio"
            }))
            yield color1
        return color1


    # color2 = forms.ChoiceField(label='ioi', widget=forms.CheckboxInput(attrs={
    #     'autocomplete': "off",
    #     'class': "btn-check",
    #     'id': "option1",
    #     'name': "options",
    #     'type': "radio"
    # }))

