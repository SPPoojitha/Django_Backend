# Generated by Django 4.1.13 on 2024-01-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_blog_tags_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.TextField(max_length=255),
        ),
    ]
