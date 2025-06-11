from django import forms

from petstagram.common.mixins import ReadOnlyMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields =['name', 'date_of_birth', 'personal_pet_photo']

        widgets = {
            "name": forms.TextInput(
                attrs={
                    'placeholder': 'Pet Name',
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            "personal_pet_photo": forms.TextInput(
                attrs={
                    'placeholder': 'Link to Image'
                }
            )
        }

        labels = {
            "name": "Pet name",
            "date_of_birth": "Date of birth",
            "personal_pet_photo": "Link to image",
        }

class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(ReadOnlyMixin, PetBaseForm):
    pass