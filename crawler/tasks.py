import os
import re

import requests
import qrcode
from bs4 import BeautifulSoup as bs
from django.conf import settings
from django.core.files import File
from .models import News


class URL(object):
    def __init__(self, url, file_type="jpg"):
        self.origin_url = url
        self.file_type = file_type

        self.gen_tinyurl()
        self.gen_qr_img()

    def gen_tinyurl(self):
        tinyurl_api = "https://tinyurl.com/api-create.php?url="
        res = requests.get(tinyurl_api + self.origin_url)
        self.short_url = res.text
        return self.short_url

    def gen_qr_img(self):
        match = re.match('https://tinyurl.com/(.*)', self.short_url)
        hashed_id = match.group(1)
        self.file_name = ".".join([hashed_id, self.file_type])
        self.qr_img = qrcode.make(self.short_url)

def inside_crawler():
    """
    Title Crawler for www.inside.com
    """
    from io import BytesIO
    url = "https://www.inside.com.tw/category/trend"

    trend_page = requests.get(url).text
    soup = bs(trend_page, 'html.parser')
    posts = soup.select('h3.post_title a.js-auto_break_title')
    
    all_post = list()
    for post in posts:
        link = post['href']
        title = post.text
        url = URL(link)
        if News.objects.filter(short_url=url.short_url, title=title):
            continue

        news = News(
                    title=title,
                    url = url.origin_url,
                    short_url = url.short_url,
                    website_icon = "https://www.inside.com.tw/assets/wp-content/themes/inside/images/logo.svg"
                    )
        buf = BytesIO()
        url.qr_img.save(buf, format="jpeg")
        news.qr_img.save(url.file_name, File(buf))
