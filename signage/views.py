import random

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import timezone
from image_anncs.models import Image
from crawler.models import News, Weather


# Create your views here.
def index(request):
    return render(request, "index.html")

def get_content(request):
    import json
    valid_images = Image.objects.filter(start_time__lte=timezone.localtime(), end_time__gt=timezone.localtime())
    images = valid_images.order_by("-created_time")[:10]
    content = list()

    for img in images:
        html_string = render_to_string("content.html",
                                       context=dict(url=img.image.url,
                                                    type="image"))
        content.append(dict(content=html_string,
                            display_time=img.display_time))
        print(img.image.url)

    news = News.objects.order_by("-created_time")[:30]
    sample_size = 15
    sampled_idxes = random.sample(range(len(news)), sample_size)
    for i in range(sample_size//3):
        html_string = render_to_string("content.html",
                context=dict(news=[news[idx] for idx in sampled_idxes[i*3: (i+1)*3]],
                                                    type="news"))
        content.append(dict(content=html_string, display_time=10))

    weather = Weather.objects.last()
    html_string = render_to_string("content.html",
                                   context=dict(url=weather.image_link,
                                                type="image"))
    content.append(dict(content=html_string, display_time=weather.display_time))


    random.shuffle(content)
    return HttpResponse(json.dumps(content))

