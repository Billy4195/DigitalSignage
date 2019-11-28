from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    model = News
admin.site.register(News, NewsAdmin)
