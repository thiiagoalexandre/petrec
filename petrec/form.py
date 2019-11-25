from django import forms
from .models import Cachorro, Usuario


class AddDog(forms.ModelForm):
    class Meta:
        model = Cachorro
        fields = '__all__'


class AddUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
