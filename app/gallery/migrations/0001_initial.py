# Generated by Django 3.2.7 on 2021-10-06 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Photo Category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name Photo')),
                ('place', models.CharField(blank=True, max_length=100, verbose_name='Photo Spot')),
                ('camera', models.CharField(blank=True, max_length=100, verbose_name='Camera')),
                ('lens', models.CharField(blank=True, max_length=100, verbose_name='Lens')),
                ('speed', models.CharField(blank=True, max_length=10, verbose_name='Speed')),
                ('iso', models.CharField(blank=True, max_length=10, verbose_name='ISO')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('category', models.ManyToManyField(blank=True, to='gallery.Category')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
