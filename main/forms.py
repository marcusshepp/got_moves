from django import forms

from .models import (
    Move,
    Comment,
)


class MoveForm(forms.ModelForm):
    class Meta:
        model = Move
        fields = ["name", "youtube_link", "user"]
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "user"]