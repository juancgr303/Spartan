# Generated by Django 3.2.7 on 2021-10-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211005_0956'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticleManager',
        ),
        migrations.AlterField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]