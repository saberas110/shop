from django import forms
from .models import AvailableColor, Comment


class CommentForm(forms.Form):
    # star5 = forms.CharField(widget=forms.TextInput(attrs={
    #     "id": "star5",
    #     'name': "rating",
    #     'type': "radio",
    #     'value': "5",
    # }))
    # star4 = forms.CharField(label='', widget=forms.TextInput(attrs={
    #     "id": "star4",
    #     'name': "rating",
    #     'type': "radio",
    #     'value': "4",
    # }))
    # star3 = forms.CharField(label='', widget=forms.TextInput(attrs={
    #     "id": "star3",
    #     'name': "rating",
    #     'type': "radio",
    #     'value': "3",
    # }))
    # star2 = forms.CharField(label='', widget=forms.TextInput(attrs={
    #     "id": "star2",
    #     'name': "rating",
    #     'type': "radio",
    #     'value': "2",
    # }))
    # star1 = forms.CharField(label='', widget=forms.TextInput(attrs={
    #     "id": "star1",
    #     'name': "rating",
    #     'type': "radio",
    #     'value': "1",
    # }))
    text = forms.CharField(widget=forms.Textarea(attrs={
    'class' :"form-control",
    'id' : "floatingTextarea2",
    'placeholder' : "Leave a comment here",
    'style' : "height: 150px",
    }))
    positive_point = forms.CharField(widget=forms.TextInput(attrs={
    'class' :"commentTags form-control",
    'id' : "tags-pos",
    'name' : "tags-pos",
    'placeholder' : "با کلید اینتر اضافه کنید",
    }))
    negative_point = forms.CharField(widget=forms.TextInput(attrs={
        'class': "commentTags form-control",
        'id': "tags-neg",
        'name': "tags-neg",
        'placeholder': "با کلید اینتر اضافه کنید",
    }))


