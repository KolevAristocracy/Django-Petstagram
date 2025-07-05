from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.common.mixins import UserIsOwnerMixin
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.

class AddPetView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

# def pets_add(request: HttpRequest) -> HttpResponse:
#     form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1) # That's because we don't have users yet
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, template_name='pets/pet-add-page.html', context=context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'  # this we can ignore because django by default takes the model name (Pet) in lowercase
    slug_url_kwarg = 'pet_slug'  # help pets/urls to know that the slug is named - 'pet_slug'

    def get_context_data(self, **kwargs):
        # Option 1 given by the lecturer
        kwargs.update({
            "comment_form": CommentForm(),
            "all_photos": self.object.photo_set.prefetch_related('tagged_pets', 'like_set').all(),
        })
        return super().get_context_data(**kwargs)

        # Option 2
        # context = super().get_context_data(**kwargs)
        # context['all_photos'] = self.object.photo_set.prefetch_related('tagged_pets', 'like_set').all()
        # context['comment_form'] = CommentForm()
        # return context

# def pets_details(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.prefetch_related('tagged_pets', 'like_set').all()
#     comment_form = CommentForm()
#     context  = {
#         "pet": pet,
#         "all_photos": all_photos,
#         "comment_form": comment_form,
#     }
#
#     return render(request, template_name='pets/pet-details-page.html', context=context)


class EditPetView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self) -> str:
        return reverse_lazy(
            'pets-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug'],
            }
        )



# def pets_edit(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('pets-details', username=username, pet_slug=pet_slug)
#
#     context = {
#         "pet": pet,
#         "form": form
#     }

    # return render(request, template_name='pets/pet-edit-page.html', context=context)

class DeletePetView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    slug_url_kwarg = "pet_slug"
    form_class = PetDeleteForm

    def get_initial(self) -> dict:
        return self.object.__dict__

    # Option 1
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"data": self.get_initial()})
        return kwargs

    # Option 2
    # def post(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)

# def pets_delete(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetDeleteForm(instance=pet)
#
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile-details', pk=1)
#
#     context = {
#         "pet": pet,
#         "form": form,
#     }
#
#     return render(request, template_name='pets/pet-delete-page.html', context=context)
