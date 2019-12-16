from django.db import models
from django.utils import timezone
from datetime import timedelta

def seven_days_after_today():
    return timezone.localtime() + timedelta(days=7)

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(u'建立時間', auto_now_add=True)
    updated_time = models.DateTimeField(u'更新時間', auto_now=True)
    image = models.ImageField(upload_to='image')
    display_time = models.IntegerField(u'播放時間', default=5)
    start_time = models.DateTimeField(u'開始播放時間', blank=True, default=timezone.localtime)
    end_time = models.DateTimeField(u'結束播放時間', blank=True,
            default=seven_days_after_today)

    class Meta:
        verbose_name = '圖片公告'
        verbose_name_plural = '圖片公告'

