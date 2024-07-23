from django.db import models

# Create your models here.

class Movie(models.Model):
    
    Name = models.CharField(max_length= 250)
    Year = models.IntegerField()
    Description = models.TextField()
    image = models.ImageField(upload_to= 'static/img')

    def __str__(self):
        return self.Name