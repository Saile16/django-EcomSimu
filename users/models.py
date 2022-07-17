from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):    
    #para conectar el usuario al profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='profile.jpg',upload_to='profile_pictures')
    contact_number=models.CharField(max_length=10,default='999999999')
    
    def __str__(self):
        return self.user.username