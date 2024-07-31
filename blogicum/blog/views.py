from django.shortcuts import get_object_or_404, render
from blog.models import Category, Post
from django.http import Http404
from django.utils import timezone


def index(request):
    post_list = Post.objects.all().filter(
        created_at__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )[:5]
    context = {'post_list': post_list}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, pk=post_id)
    if not post.is_published or post.created_at > timezone.now():
        raise Http404('Публикция не найдена')
    context = {'post': post, 'current_view': 'post_detail'}
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published: 
        raise Http404("Категория не найдена")
    post_list = Post.objects.filter(category=category).filter(
        created_at__lte=timezone.now(),
        is_published=True).order_by('created_at')
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })
