from django import forms


from .models import (
    Classic,
)


class ClassicForm(forms.ModelForm):
    class Meta:
        model = Classic
        fields = [
            "name",
            "youtube_link",
            "user",
            "description",
            "placeholder_image",
            "credits",
            "estimated_creation_date",
            "category",
        ]
