from django.shortcuts import render
from .models import *

# INDEX - HOME

def home(request):           
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated') 
    profiles = Profile.objects.filter(about=about) 
    categories = Category.objects.all()   

    context = {
        'home': home,
        'about': about,
        'profiles' : profiles,
        'categories' : categories,        
    }
    return render(request, 'home/home.html', context)


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def contact(request):
    return render(request, 'contact/contact.html')
