from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    Img=models.ImageField(max_length=250)
    Description=models.TextField()


    def __str__(self):
        return self.name
class Team(models.Model):
    nam=models.CharField(max_length=250)
    Image=models.ImageField(max_length=250)
    Dsc=models.TextField()

    def __str__(self):
        return self.nam