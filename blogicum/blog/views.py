from django.shortcuts import render


def index(request):
    context = {'posts': list(reversed(posts)), 'current_view': 'index'}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = post_dict.get(post_id)
    if post is None:
        template = 'blog/error404.html'
    context = {'post': post, 'current_view': 'post_detail'}
    return render(request, template, context)


def category_posts(request, category_slug):
    context = {'category_slug': category_slug}
    template = 'blog/category.html'
    return render(request, template, context)
