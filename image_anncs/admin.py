from django.contrib import admin
from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    model = Image
admin.site.register(Image, ImageAdmin)
