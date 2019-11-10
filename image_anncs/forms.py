from django import forms
from .models import Image
from django.forms import ModelForm

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['created_time', 'updated_time', 'id']

