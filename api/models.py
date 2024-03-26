from django.db import models
from django.utils import timezone
import json

# Create your models here.

class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self):
       return self.locationName
    

class Tag(models.Model):
    tagName = models.CharField(max_length=100, unique=True)
    tagDate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.tagName

class Source(models.Model):
    source_name=models.CharField(max_length=100)
    source_type= models.CharField(max_length=100)

    def __str__(self):
        return self.source_name


class Item(models.Model):
    itemName=    models.CharField(max_length=100, unique=True)
    date_added= models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location,on_delete=models.CASCADE)
    itemWeight = models.BigIntegerField(default=0)
    isInside = models.BooleanField(default= False)
    tags = models.ManyToManyField(Tag,blank=True)
    source =  models.ForeignKey(Source,on_delete=models.CASCADE,null=True)


    def __str__(self):
       return self.itemName