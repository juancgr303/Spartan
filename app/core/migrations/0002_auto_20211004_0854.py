# Generated by Django 3.2.7 on 2021-10-04 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='heading',
            field=models.CharField(max_length=50, verbose_name='Heading or greetings'),
        ),
        migrations.AlterField(
            model_name='home',
            name='picture',
            field=models.ImageField(max_length=10, upload_to='static/img/home', verbose_name='Your Photo'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=10)),
                ('link', models.URLField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.about')),
            ],
        ),
    ]
