# Generated by Django 3.2.7 on 2021-10-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_home_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=30),
        ),
    ]
