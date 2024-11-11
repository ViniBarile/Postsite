from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    capa_url = models.URLField(max_length=200, null=True)
    data_postagem = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    def __str__(self):
        return f'{self.name} ({self.release_year})'
