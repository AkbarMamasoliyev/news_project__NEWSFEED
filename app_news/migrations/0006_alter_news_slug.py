# Generated by Django 5.1.1 on 2024-09-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_alter_news_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
