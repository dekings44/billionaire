from django import forms
from .models import Billionaires


class PostForm(forms.ModelForm):
    class Meta:
        model = Billionaires
        fields = ['name', 'money', 'source', 'description']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'money' : forms.TextInput(attrs={'class': 'form-control'}),
            'source' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }