from .models import Post, Comment
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm, CommentForm
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ['name', 'release_year', 'capa_url', 'content']
    success_url = reverse_lazy('posts:index')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['name', 'release_year', 'capa_url', 'content']
    def get_success_url(self):
        return reverse('posts:detail', args=[self.object.id])

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)
