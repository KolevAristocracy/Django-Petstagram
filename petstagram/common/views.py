from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.

class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    ordering = 'date_of_publication'
    paginate_by = 2

    def get_context_data(self, *, object_list = None, **kwargs):
        # Option 2 given by the lecturer
        kwargs.update({
            "comment_form": CommentForm(),
            "search_form": SearchForm(),
        })
        return super().get_context_data(object_list=object_list, **kwargs)

        # Option 1
        # context = super().get_context_data(**kwargs)
        # context['comment_form'] = CommentForm()
        # context['search_form'] = SearchForm(self.request.GET)
        # return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('text')

        if pet_name:
            queryset = queryset.prefetch_related('tagged_pets', 'like_set').filter(
                tagged_pets__name__icontains=pet_name
            )

        return queryset

# def home_page(request: HttpRequest) -> HttpResponse:
#     comment_form = CommentForm()
#     search_form = SearchForm(request.GET or None)
#
#     if search_form.is_valid():
#         all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').filter(
#             tagged_pets__name__icontains=search_form.cleaned_data.get('text', '')
#         )
#     else:
#         all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()
#
#     photos_per_page = 1
#     paginator = Paginator(all_photos, photos_per_page)
#     page = request.GET.get('page')
#
#     try:
#         all_photos = paginator.page(page)
#     except PageNotAnInteger:
#         all_photos = paginator.page(1)
#     except EmptyPage:
#         all_photos = paginator.page(paginator.num_pages)
#
#     context = {
#         "all_photos": all_photos,
#         "comment_form": comment_form,
#         "search_form": search_form,
#     }
#
#     return render(request, template_name='common/home-page.html', context=context)

def like(request: HttpRequest, photo_id: int) -> HttpResponse:
    like_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()  # [QuerySet]

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id,
            user=request.user,
        )

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")

def share(request: HttpRequest, photo_id: int):
    # pip-install pyperclip
    # This will only work locally

    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")

def add_comment(request: HttpRequest, photo_id: int) -> HttpResponse:
    form = CommentForm(request.POST or None)


    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = Photo.objects.get(pk=photo_id)
        comment.user = request.user
        comment.save()

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")