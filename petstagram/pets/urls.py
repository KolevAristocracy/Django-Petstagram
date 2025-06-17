from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.AddPetView.as_view(), name='pets-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsView.as_view(), name='pets-details'),
        path('edit/', views.EditPetView.as_view(), name='pets-edit'),
        path('delete/', views.DeletePetView.as_view(), name='pets-delete'),
    ]))
]