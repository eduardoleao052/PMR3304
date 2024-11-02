from django import forms
from . import models
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','banner','private']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'body',
        ]
        labels = {
            'body': 'Comment',
        }