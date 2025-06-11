from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.
def photo_add(request) -> HttpResponse:
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        "form": form,
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)

def photo_edit(request, pk) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        "photo": photo,
        "form": form,
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)

def photo_details(request, pk) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        "photo": photo,
        "comments": comments,
        "comment_form": comment_form,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)

def photo_delete(request: HttpRequest, pk:int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')