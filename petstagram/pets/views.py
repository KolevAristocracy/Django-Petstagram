from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
def pets_add(request: HttpRequest) -> HttpResponse:
    form = PetCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile-details', pk=1) # That's because we don't have users yet

    context = {
        "form": form,
    }

    return render(request, template_name='pets/pet-add-page.html', context=context)

def pets_details(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.prefetch_related('tagged_pets', 'like_set').all()
    comment_form = CommentForm()
    context  = {
        "pet": pet,
        "all_photos": all_photos,
        "comment_form": comment_form,
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)

def pets_edit(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pets-details', username=username, pet_slug=pet_slug)

    context = {
        "pet": pet,
        "form": form
    }

    return render(request, template_name='pets/pet-edit-page.html', context=context)

def pets_delete(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        "pet": pet,
        "form": form,
    }

    return render(request, template_name='pets/pet-delete-page.html', context=context)
