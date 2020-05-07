from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from . import views


urlpatterns = [
    path('signup/', staff_member_required(views.SignUp.as_view()), name='signup'),
    path('profile/', views.Profile, name='profile'),
]
