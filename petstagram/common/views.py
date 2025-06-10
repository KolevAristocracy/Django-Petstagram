from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.
def home_page(request) -> HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()

    context = {
        "all_photos": all_photos
    }

    return render(request, template_name='common/home-page.html', context=context)

def like(request, photo_id: int) -> HttpResponse:
    like_object = Like.objects.filter(to_photo_id=photo_id).first()  # [QuerySet]

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id
        )

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")

def share(request, photo_id):
    # pip install pyperclip
    # This will only work locally

    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")
