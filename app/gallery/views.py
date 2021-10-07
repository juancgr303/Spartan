from django.shortcuts import render, redirect
from .models import *
from core.models import Home


def gallery(request):
    category = request.GET.get('Category')
    if category == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name=category)    
    home = Home.objects.latest('updated')   
    categories = Category.objects.all()   
    context = {
        'home': home,
        'images': images,        
        'categories': categories,
    }
        
    return render(request, "gallery/gallery.html", context)

def viewPhot(request, pk):
    images = Image.objects.get(id=pk)
    home = Home.objects.latest('updated')   
    categories = Category.objects.all()
    context = {
        'home': home,
        'images': images,        
        'categories': categories,
    }
    return render(request, "gallery/photo.html", context)
