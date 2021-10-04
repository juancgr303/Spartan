# Generated by Django 3.2.7 on 2021-10-04 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50, verbose_name='Heading or greetins')),
                ('career', models.CharField(max_length=50, verbose_name='Career')),
                ('description', models.TextField(verbose_name='Description')),
                ('profile_img', models.ImageField(upload_to='static/img/home', verbose_name='Your profile photo')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Profession')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name of Page')),
                ('acronym', models.CharField(max_length=2, verbose_name='Acronym of Name')),
                ('title', models.CharField(max_length=20, verbose_name='Title of Page')),
                ('instagram_url', models.URLField(verbose_name='Your instagram url')),
                ('github_url', models.URLField(verbose_name='Your Git-Hub url')),
                ('greetings_1', models.CharField(max_length=5, verbose_name='Greetings in page 1st')),
                ('greetings_2', models.CharField(max_length=5, verbose_name='Greetings in page 2nd')),
                ('picture', models.ImageField(max_length=5, upload_to='static/img/home', verbose_name='Your Photo')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.URLField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
    ]
