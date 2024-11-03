from django import forms
from . import models
from .models import Post

class CreatePost(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=models.Categories.objects.all())
    class Meta:
        model = models.Post
        fields = ['title','body','banner','private','categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'body',
        ]
        labels = {
            'body': 'Comment',
        }