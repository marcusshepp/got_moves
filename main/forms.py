from django import forms

from .models import (
    Move,
    Comment,
    Performance,
    Category,
    Comment,
    Profile,
)


class MoveForm(forms.ModelForm):
    class Meta:
        model = Move
        fields = (
            "name",
            "youtube_link",
            "user",
            "tutorial",
            "private",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "text",
            "user",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "description",
            "first_name",
            "last_name",
            "email",
            "inspiration",
            "url",
        )


class CategoryForm(forms.ModelForm):
            model = Category
            fields = (
                "name",
            )
