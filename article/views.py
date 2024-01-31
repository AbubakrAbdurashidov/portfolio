from django.shortcuts import render, get_object_or_404, redirect

from article.models import Article, Category, Tag, Comment
from .forms import CommentForm
from django.core.paginator import Paginator
from django.contrib import messages


def blog_view(request):
    articles = Article.objects.order_by('-id')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    txt = ' '
    page_obj = paginator.get_page(page)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    sidebar_articles = Article.objects.order_by('-id')[:3]
    if q:
        page_obj = articles.filter(title__icontains=q)
    if cat:
        page_obj = articles.filter(category__title__exact=cat)
        txt = cat
    if tag:
        page_obj = articles.filter(tags__title__exact=tag)
    ctx = {
        'page_obj': page_obj,
        'articles': articles,
        'sidebar_articles': sidebar_articles,
        'categories': categories,
        'title': txt,
        'tags': tags
    }
    return render(request, 'article/blog.html', ctx)


def detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    categories = Category.objects.all()
    form = CommentForm()
    tags = Tag.objects.all()
    sidebar_articles = Article.objects.order_by('-id')[:3]
    parent_id = request.GET.get('p_id')
    articles = Article.objects.order_by('-id')
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)

    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            if parent_id:
                obj.parent_comment = Comment.objects.get(id=parent_id)
            obj.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('.#redirect_window')
    ctx = {
        'object_list': articles,
        'article': article,
        'form': form,
        'sidebar_articles': sidebar_articles,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'article/single.html', ctx)