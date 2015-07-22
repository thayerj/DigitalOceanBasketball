from django import forms

class NameForm(forms.Form):
    Name = forms.CharField(label='Your name', max_length=30, required=False)