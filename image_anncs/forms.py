from django import forms
from .models import Image
from django.forms import ModelForm

class ImageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({"class": "show-for-sr",
                                                  "id": "imageUpload"})

    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['created_time', 'updated_time', 'id']

