# forms.py
from django import forms
from .models import Car, Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('title', )

PostImageFormSet = forms.inlineformset_factory(Car, Image, form=ImageForm, extra=1)
