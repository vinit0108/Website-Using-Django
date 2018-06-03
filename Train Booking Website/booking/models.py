from django.db import models

# Create your models here.
class Booking(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    adult = models.CharField(max_length=50)
    child = models.CharField(max_length=50)
    age = models.CharField(max_length=50)