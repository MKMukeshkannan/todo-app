from django import forms

class todoForm(forms.Form):
    Task = forms.CharField(max_length=200)
