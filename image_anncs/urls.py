from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
        path('upload/', views.upload, name='upload'),
        path('delete/<int:img_id>', views.delete, name='img_delete'),
]
