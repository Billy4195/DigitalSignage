from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(u'建立時間', auto_now_add=True)
    updated_time = models.DateTimeField(u'更新時間', auto_now=True)
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name = '圖片公告'
        verbose_name_plural = '圖片公告'

