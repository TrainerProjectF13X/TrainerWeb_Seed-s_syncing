from django import forms

from .models import Post as Po


class PostForm(forms.ModelForm):
    class Meta:
        model = Po
        fields = [
            "title",
            'content'
        ]
