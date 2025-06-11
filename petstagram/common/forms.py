from django import forms
from django.forms.widgets import TextInput

from petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Add a comment ...',
                    'cols': 40,
                    'rows': 10,

                }
            )
        }


class SearchForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        required=False,
        widget=TextInput(
            attrs={
                'placeholder': 'Search by pet name ...'
            }

        )
    )

"""
<input type="text" placeholder="Search by pet name...">
"""