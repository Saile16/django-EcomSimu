from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return self.name

