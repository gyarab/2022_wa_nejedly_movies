# Generated by Django 4.1.7 on 2023-06-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_remove_movie_comments_comment_movie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='photo_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
