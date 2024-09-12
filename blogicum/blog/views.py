from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Category, Post

NUMBER_POSTS = 5


def get_queryset():
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    post_list = get_queryset()[:NUMBER_POSTS]
    context = {'post_list': post_list}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, id=post_id, is_published=True,
                             pub_date__lte=timezone.now())
    if (not post.is_published or post.created_at > timezone.now()
            or not post.category.is_published):
        raise Http404('Публикция не найдена')
    context = {'post': post, 'current_view': 'post_detail'}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = get_queryset().filter(
        category=category)
    return render(request, template, {
        'category': category,
        'post_list': post_list
    })
