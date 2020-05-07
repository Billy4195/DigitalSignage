from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image

@login_required
def upload(request):
    form = ImageForm(request.POST.copy() or None, request.FILES or None)
    if request.method == "POST":
        if request.user.is_authenticated:
            form.data['user'] = request.user

        if form.is_valid():
            msg_suc = "Upload image success!"
            form.save()
        else:
            msg_warn = "Upload fail!"
    return render(request, "upload.html", locals())

def delete(request, img_id):
    img = Image.objects.filter(id=img_id)
    if request.method == "POST":

        return redirect('profile')
    elif request.method == "GET":

        return render(request, 'delete.html', locals())
