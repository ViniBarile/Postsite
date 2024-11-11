from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_posts, name='index'), # adicione esta linha
    path('search/', views.search_posts, name='search'),
    path('create/', views.create_post, name='create'),
    path('<int:post_id>/', views.detail_post, name='detail'),

]