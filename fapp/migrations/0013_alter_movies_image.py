# Generated by Django 5.0.6 on 2024-07-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0012_alter_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]