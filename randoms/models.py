from django.db import models

# Create your models here.
class Hero(models.Model):

    name = models.CharField(max_length=200)
    types = models.CharField(max_length=100, default="")
    images = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.name} - {self.types} - {self.images}"
    
