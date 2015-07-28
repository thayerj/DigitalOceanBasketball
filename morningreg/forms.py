from django import forms

class NameForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=30, required=False)