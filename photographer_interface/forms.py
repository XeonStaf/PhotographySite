from django import forms

from portfolio.models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('album',)
