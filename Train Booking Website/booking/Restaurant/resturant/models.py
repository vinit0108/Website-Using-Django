from django.db import models

# Create your models here.

class rest(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    dishes = models.CharField(max_length=300)
    rating = models.IntegerField(max_length=100)
    def __str__(self):
       return self.name