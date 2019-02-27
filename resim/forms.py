from django import forms
from .models import Resim

class PostForm(forms.ModelForm):

    class Meta:
        model = Resim
        fields = [
            'title',
            'image',
        ]