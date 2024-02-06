from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    image=models.ImageField(upload_to="images/places",null=True,blank=True)
    def __str__(self):
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    image=models.ImageField(upload_to="images/places",null=True,blank=True)
    def __str__(self):
        return self.name