from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def photo_add(request) -> HttpResponse:
    return render(request, template_name='photos/photo-add-page.html')

def photo_edit(request, pk) -> HttpResponse:
    return render(request, template_name='photos/photo-edit-page.html')

def photo_details(request, pk) -> HttpResponse:
    return render(request, template_name='photos/photo-details-page.html')
