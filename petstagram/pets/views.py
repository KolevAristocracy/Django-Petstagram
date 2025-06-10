from django.http import HttpResponse
from django.shortcuts import render

from petstagram.pets.models import Pet


# Create your views here.
def pets_add(request) -> HttpResponse:
    return render(request, template_name='pets/pet-add-page.html')

def pets_details(request, username, pet_slug) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.prefetch_related('tagged_pets', 'like_set').all()

    context  = {
        "pet": pet,
        "all_photos": all_photos,
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)

def pets_edit(request) -> HttpResponse:
    return render(request, template_name='pets/pet-edit-page.html')

def pets_delete(request) -> HttpResponse:
    return render(request, template_name='pets/pet-delete-page.html')
