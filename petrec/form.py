from django.forms.widgets import ClearableFileInput
from django import forms
from .models import TB_Cachorro


class AddDog(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = TB_Cachorro
        fields = '__all__'
