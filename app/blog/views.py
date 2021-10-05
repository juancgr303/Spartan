from django.shortcuts import get_object_or_404, render, HttpResponsePermanentRedirect
from .models import *
from core.models import Home
# Django Q objects use to create complex queries
# https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects
from django.db.models import Q

def blog(request):
    home = Home.objects.latest('updated')
    # Featured articles on the home page
    featured = Article.articlemanager.filter(featured=True)    
    context = {
        'home': home,
        'articles': featured
    }
    return render(request, 'blog/blog.html', context)

def article(request, article):
    home = Home.objects.latest('updated')
    article = get_object_or_404(Article, slug=article, status='published')
    context = {
        'home': home,
        'article': article              
    }
    return render(request, 'blog/article.html', context)

def articles(request):
    home = Home.objects.latest('updated')
    # Get query from request
    query = request.GET.get('query')
    # Print(query)
    # Set query to '' if None
    if query == None:
        query = ''    
    #articles = Article.articlemanager.all()
    # Search for query in headline, sub headline, body
    articles = Article.articlemanager.filter(
        Q(headline__icontains=query) |
        Q(sub_headline__icontains=query) |
        Q(body__icontains=query)
    )
    tags = Tag.objects.all()

    context = {
        'home': home,
        'articles': articles,
        'tags': tags,
    }
    return render(request, 'blog/articles.html', context)