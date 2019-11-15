from django.shortcuts import render
from image_anncs.models import Image

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_content(request):
    from django.http import HttpResponse
    import json
    images = Image.objects.all()
    content = {
        'urls': [im.image.url for im in images]
    }
    return HttpResponse(json.dumps(content))

