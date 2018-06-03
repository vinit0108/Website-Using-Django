from django.db import models

# Create your models here.

class Employe(models.Model):
    # title of the watch
    title = models.CharField(max_length=100)
    # description of the watch
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3= models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)

    def __str__(self):
       return self.title


def __str__(self):
    return self.title1

def __str__(self):
       return self.title2
def __str__(self):
       return self.title3
def __str__(self):
       return self.title4
def __str__(self):
       return self.title5

