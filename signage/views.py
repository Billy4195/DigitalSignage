from django.shortcuts import render
from image_anncs.models import Image

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_content(request):
    from django.http import HttpResponse
    import json
    images = Image.objects.all()
    content = list()
    for img in images:
        content.append(dict(url=img.image.url,
                            display_time=img.display_time))
    return HttpResponse(json.dumps(content))

