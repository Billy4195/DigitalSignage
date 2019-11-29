from django.db import models

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(u'建立時間', auto_now_add=True)
    updated_time = models.DateTimeField(u'更新時間', auto_now=True)
    title = models.CharField(u'標題', max_length=2000)
    url = models.CharField(u'網址', max_length=2000)
    short_url = models.CharField(u'短網址', max_length=100)
    website_icon = models.CharField(u'網站圖示', max_length=2000)
    qr_img = models.ImageField(u'QR code檔案路徑', upload_to="news")

    class Meta:
        verbose_name = '新聞'
        verbose_name_plural = '新聞'

class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(u'建立時間', auto_now_add=True)
    updated_time = models.DateTimeField(u'更新時間', auto_now=True)
    image_link = models.CharField(u'圖片連結', max_length=2000)
    display_time = models.IntegerField(u'播放時間', default=8)

    class Meta:
        verbose_name = '天氣資訊'
        verbose_name_plural = '天氣資訊'

