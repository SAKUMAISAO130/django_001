from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import FileUpload

from .forms import FileUploadForm


def index(request):
    file_obj = FileUpload.objects.all()
    return render(request, 'calculate/index.html', {'file_obj': file_obj})


def new_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('calculate:index')
    else:
        form = FileUploadForm()
    return render(request, 'calculate/new_file.html', {'form': form })