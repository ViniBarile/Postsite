from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'release_year',
            'capa_url',
            'content',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Data de Lançamento',
            'capa_url': 'URL da Capa',
            'content': 'Sinopse',
        }