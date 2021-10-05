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



def photography(request):
    return render(request, 'photography/photography.html')


def porfolio(request):
    return render(request, 'porfolio/porfolio.html')


def contact(request):
    return render(request, 'contact/contact.html')
