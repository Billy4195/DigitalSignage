from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from django.contrib.auth.decorators import login_required


@login_required
def upload(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            msg_suc = "Upload image success!"
            form.save()
        else:
            msg_warn = "Upload fail!"
    return render(request, "upload.html", locals())

