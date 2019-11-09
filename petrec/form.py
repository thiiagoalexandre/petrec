from django.forms.widgets import ClearableFileInput
from django import forms
from .models import Cachorro


class AddDog(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Cachorro
        fields = '__all__'
