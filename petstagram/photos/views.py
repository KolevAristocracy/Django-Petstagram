from django.http import HttpResponse
from django.shortcuts import render

from petstagram.photos.models import Photo


# Create your views here.
def photo_add(request) -> HttpResponse:
    return render(request, template_name='photos/photo-add-page.html')

def photo_edit(request, pk) -> HttpResponse:
    return render(request, template_name='photos/photo-edit-page.html')

def photo_details(request, pk) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()

    context = {
        "photo": photo,
        "comments": comments,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)
