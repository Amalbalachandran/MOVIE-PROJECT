# Generated by Django 5.0.6 on 2024-07-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0004_alter_movies_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Img',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]