from .models import Post
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


def list_posts(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

def create_post(request):
    if request.method == 'POST':
        post_name = request.POST['name']
        post_release_year = request.POST['release_year']
        post_content = request.POST['content']
        post_capa_url = request.POST['capa_url']
        post = Post(name=post_name, release_year=post_release_year, content=post_content, capa_url=post_capa_url)
        post.save()
        return HttpResponseRedirect(reverse('posts:detail', args=[post.id]))
    else:
        return render(request, 'posts/create.html', {})
    
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.name = request.POST['name']
        post.release_year = request.POST['release_year']
        post.content = request.POST['content']
        post.capa_url = request.POST['capa_url']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    context = {'post': post}
    return render(request, 'posts/update.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))
    context = {'post': post}
    return render(request, 'posts/delete.html', context)