# Generated by Django 5.0.6 on 2024-07-08 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0015_alter_movies_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='Img',
            new_name='image',
        ),
    ]