from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    capa_url = models.URLField(max_length=200, null=True)
    data_postagem = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name="posts")
    def __str__(self):
        return f'{self.name} ({self.release_year})'
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
