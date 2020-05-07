import random

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import timezone
from image_anncs.models import Image
from crawler.models import News, Weather

from .helper import get_display

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_content(request, content_type):
    import json
    print(content_type)
    if content_type == "display":
        content = get_display()
    elif content_type == "weather":
        """
        weather = Weather.objects.last()
        html_string = render_to_string("content.html",
                                       context=dict(url=weather.image_link,
                                                    type="image"))
        content.append(dict(content=html_string, display_time=weather.display_time))
        """

    random.shuffle(content)
    return HttpResponse(json.dumps(content))

