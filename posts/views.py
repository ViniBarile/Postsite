from .models import Post
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from .temp_data import post_data

def detail_post(request, post_id):
    post = post_data[post_id - 1]
    return HttpResponse(
        f'Detalhes do livro {post["name"]} ({post["release_year"]})')

def list_posts(request):
    context = {"post_list": post_data}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    context = {'post': post_data[post_id - 1]}
    return render(request, 'posts/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "post_list": [
                m for m in post_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'posts/search.html', context)

def create_post(request):
    if request.method == 'POST':
        post_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'capa_url': request.POST['capa_url']
        })
        return HttpResponseRedirect(
            reverse('posts:detail', args=(len(post_data), )))
    else:
        return render(request, 'posts/create.html', {})
