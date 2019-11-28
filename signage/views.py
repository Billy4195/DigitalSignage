import random

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from image_anncs.models import Image
from crawler.models import News


# Create your views here.
def index(request):
    return render(request, "index.html")

def get_content(request):
    import json
    images = Image.objects.order_by("-created_time")[:10]
    content = list()
    for img in images:
        html_string = render_to_string("content.html",
                                       context=dict(url=img.image.url,
                                                    type="image"))
        content.append(dict(content=html_string,
                            display_time=img.display_time))
    news = News.objects.order_by("-created_time")[:30]
    sample_size = 15
    sampled_idxes = random.sample(range(len(news)), sample_size)
    for i in range(sample_size//3):
        html_string = render_to_string("content.html",
                context=dict(news=[news[idx] for idx in sampled_idxes[i*3: (i+1)*3]],
                                                    type="news"))
        content.append(dict(content=html_string, display_time=10))
    random.shuffle(content)
    return HttpResponse(json.dumps(content))

