import datetime

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


def get_published_posts(category_slug=None):
    posts = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        pub_date__lt=datetime.datetime.now(),
        is_published=True,
        category__is_published=True
    )
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    return posts


def index(request):
    return render(
        request, 'blog/index.html',
        {'posts': get_published_posts()[:5]})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        pk=post_id,
        pub_date__lt=datetime.datetime.now(),
        is_published=True,
        category__is_published=True)
    return render(request, 'blog/detail.html',
                  {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': get_published_posts(category_slug=category_slug)})
