from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Category


def get_published_posts(right_posts: QuerySet):
    posts = right_posts.select_related(
        'category', 'location', 'author'
    ).filter(
        pub_date__lt=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return posts


def index(request):
    return render(
        request, 'blog/index.html',
        {'posts': get_published_posts(Post.objects.all())[:5]})


def post_detail(request, post_id):
    try:
        return render(
            request, 'blog/detail.html',
            {'post': get_published_posts(Post.objects.all()).get(pk=post_id)})
    except Post.DoesNotExist:
        raise Http404('Поста с указанным номером не существует')


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': get_published_posts(Post.objects.filter(category=category))})
