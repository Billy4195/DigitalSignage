from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
        path('get_content/<str:content_type>', views.get_content, name='get_content'),
        path('', views.index, name='home'),
]
