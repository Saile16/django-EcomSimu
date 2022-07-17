from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    #al poner el default en 1 decimos que el vendendor por default sera el que tenga el id 1
    seller_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name= models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return self.name

