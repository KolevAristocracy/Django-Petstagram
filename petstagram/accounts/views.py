from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(request) -> HttpResponse:
    return render(request, template_name='accounts/register-page.html')

def login(request) -> HttpResponse:
    return render(request, template_name='accounts/login-page.html')

def show_profile_details(request, pk: int) -> HttpResponse:
    return render(request, template_name='accounts/profile-details-page.html')

def edit_profile(request, pk: int) -> HttpResponse:
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk: int) -> HttpResponse:
    return render(request, template_name='accounts/profile-delete-page.html')
