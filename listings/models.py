from django.db import models

# Create your models here.


class Listings(models.Model):
    title = models.CharField(max_length=100)
    address= models.TextField(max_length=500)
    city= models.CharField(max_length=100)
    Zipcode = models.CharField(max_length=10)
    description= models.TextField(max_length=1000)
    price=models.BigIntegerField()
    bedrooms= models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.BooleanField()
    sqft = models.BigIntegerField()
    list_date = models.DateField()
    photo_main = models.ImageField(upload_to='media',null=True,blank=True)
    photo_1 = models.ImageField(upload_to='media',null=True,blank=True)
    photo_2 = models.ImageField(upload_to='media',null=True,blank=True)
    photo_3 = models.ImageField(upload_to='media',null=True,blank=True)
    photo_4 = models.ImageField(upload_to='media',null=True,blank=True)
    photo_5 = models.ImageField(upload_to='media',null=True,blank=True)

    def __str__(self):
        return self.title
    