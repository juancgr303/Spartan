from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def blog(request):
    return render(request, 'blog/blog.html')


def photography(request):
    return render(request, 'photography/photography.html')


def porfolio(request):
    return render(request, 'porfolio/porfolio.html')


def contact(request):
    return render(request, 'contact/contact.html')
