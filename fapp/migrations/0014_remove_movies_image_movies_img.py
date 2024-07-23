# Generated by Django 5.0.6 on 2024-07-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0013_alter_movies_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='image',
        ),
        migrations.AddField(
            model_name='movies',
            name='Img',
            field=models.ImageField(default=1, upload_to='media/static/img'),
            preserve_default=False,
        ),
    ]
