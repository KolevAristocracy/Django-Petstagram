from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def pets_add(request) -> HttpResponse:
    return render(request, template_name='pets/pet-add-page.html')

def pets_details(request) -> HttpResponse:
    return render(request, template_name='pets/pet-details-page.html')

def pets_edit(request) -> HttpResponse:
    return render(request, template_name='pets/pet-edit-page.html')

def pets_delete(request) -> HttpResponse:
    return render(request, template_name='pets/pet-delete-page.html')
