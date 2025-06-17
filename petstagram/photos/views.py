from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.
class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home-page')

# def photo_add(request) -> HttpResponse:
#     form = PhotoCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('home-page')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, template_name='photos/photo-add-page.html', context=context)


class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'
    context_object_name = 'photo'  # again not necessary
    success_url = reverse_lazy('home-page')


# def photo_edit(request, pk) -> HttpResponse:
#     photo = Photo.objects.get(pk=pk)
#     form = PhotoEditForm(request.POST or None, instance=photo)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('home-page')
#
#     context = {
#         "photo": photo,
#         "form": form,
#     }
#
#     return render(request, template_name='photos/photo-edit-page.html', context=context)

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            "comments":self.object.comment_set.all(),
            "comment_form": CommentForm()
        })
        return super().get_context_data(**kwargs)

# def photo_details(request, pk) -> HttpResponse:
#     photo = Photo.objects.get(pk=pk)
#     comments = photo.comment_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         "photo": photo,
#         "comments": comments,
#         "comment_form": comment_form,
#     }
#
#     return render(request, template_name='photos/photo-details-page.html', context=context)

def photo_delete(request: HttpRequest, pk:int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')