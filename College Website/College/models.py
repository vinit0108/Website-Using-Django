from django.db import models

# Create your models here.

class College(models.Model):
    # title of the watch
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # description of the watch
    area = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    field= models.CharField(max_length=100)


def __str__(self):
    return self.cid
def __str__(self):
       return self.name

def __str__(self):
    return self.area

def __str__(self):
       return self.ratings

def __str__(self):
       return self.field


