from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.db.models import Q

# post_dict = {post['id']: post for post in posts}

import datetime


def index(request):
    post_list = Post.objects.select_related('category').select_related(
        'location').select_related('author').filter(
            Q(pub_date__lt=datetime.datetime.now())
            & Q(is_published=True)
            & Q(category__is_published=True)).order_by('-pub_date')[0:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
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
    post_list = Post.objects.select_related('category').select_related(
        'location').select_related('author').filter(
        Q(category__slug=category_slug)
        & Q(pub_date__lt=datetime.datetime.now())
        & Q(is_published=True)
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {
        'category': category, 'post_list': post_list})
