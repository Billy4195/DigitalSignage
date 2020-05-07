from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from image_anncs.models import Image
from django.contrib.auth.decorators import login_required


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("signup")
    template_name = "registration/signup.html"

@login_required
def Profile(request):
    if request.user.is_staff:
        images = Image.objects.all()
    elif request.user.is_authenticated:
        images = Image.objects.filter(user=request.user)
    return render(request, "profile.html", locals())
