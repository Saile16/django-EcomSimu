from django.contrib import admin
from .models import Product
# Register your models here.

# registramos el modelo Product en el admin
admin.site.register(Product)