from django.contrib import admin
from .models import Post, Comment, Categories, PostInCategory


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categories)
admin.site.register(PostInCategory)