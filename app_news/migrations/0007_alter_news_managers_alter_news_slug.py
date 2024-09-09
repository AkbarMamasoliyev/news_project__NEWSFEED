# Generated by Django 5.1.1 on 2024-09-09 14:39

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_alter_news_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='news',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
