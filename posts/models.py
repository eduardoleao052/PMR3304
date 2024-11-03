from django.contrib.auth.models import User
from django.db import models

class Categories(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    private = models.BooleanField(default=True)
    categories = models.ManyToManyField(Categories, related_name='posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.body}" - {self.author.username}'

    
class PostInCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.post} - {self.cat}'