from logging import PlaceHolder
from django import forms
class CreateEntry(forms.Form):
    title = forms.CharField(max_length=100,required=True)
    description = forms.CharField(widget=forms.Textarea,required=True)
class SearchEntry(forms.Form):
    entry = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))
class EditEntry(forms.Form):
    body = forms.CharField(widget=forms.Textarea,required=True)