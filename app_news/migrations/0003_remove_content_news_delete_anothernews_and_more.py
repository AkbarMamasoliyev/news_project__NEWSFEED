# Generated by Django 5.1.1 on 2024-09-08 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_anothernews_alter_news_slug_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='news',
        ),
        migrations.DeleteModel(
            name='AnotherNews',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
