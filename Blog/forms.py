from django import forms
from django.core import validators
from .models import Post
from tinymce.widgets import TinyMCE

class PostModelForm(forms.ModelForm):
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    title = forms.CharField(validators=[validators.MinLengthValidator(3, message='En az 3 karakter giriniz.')])

    class Meta:
        model = Post
        fields = ['title', 'cover_image', 'category', 'content', 'tag']