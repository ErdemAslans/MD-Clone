from django.forms import ModelForm
from .models import Suport
from django import forms
from tinymce.widgets import TinyMCE


class SuportModelForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        model = Suport
        fields = ['user','email','adres','content',]