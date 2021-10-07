from django.db import models
from django.utils import timezone


class Category(models.Model):
    name =models.CharField(max_length=100, verbose_name='Photo Category')
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=60, verbose_name='Name Photo')
    place = models.CharField(max_length=100, blank=True, verbose_name='Photo Spot')
    camera = models.CharField(max_length=100, blank=True, verbose_name='Camera')
    lens = models.CharField(max_length=100, blank=True, verbose_name='Lens')
    speed = models.CharField(max_length=10, blank=True, verbose_name='Speed')
    aperture = models.CharField(max_length=10, blank=True, verbose_name='Aperture')
    iso = models.CharField(max_length=10, blank=True, verbose_name='ISO')
    image = models.ImageField(upload_to="gallery/")
    category = models.ManyToManyField(Category, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name