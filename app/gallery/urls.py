from django.urls import path
from . import views


app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhot, name='photo'),
    

]