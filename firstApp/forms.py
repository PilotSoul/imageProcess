from django import forms
from .models import ImageP


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageP
        fields = ('image',)