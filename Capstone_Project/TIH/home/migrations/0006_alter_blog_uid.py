# Generated by Django 4.1.13 on 2024-01-09 05:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_blog_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('3fbe4fb8-d230-4d9a-acee-50d8c14bae54'), editable=False, primary_key=True, serialize=False),
        ),
    ]
