from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request) -> HttpResponse:
    return render(request, template_name='common/home-page.html')
