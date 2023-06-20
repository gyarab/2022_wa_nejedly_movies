# Generated by Django 4.1.7 on 2023-05-09 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='films.movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
