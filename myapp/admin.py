from django.contrib import admin
from .models import Product
# Register your models here.

# registramos el modelo Product en el admin
admin.site.site_title='ABC Buying'
admin.site.site_header='Buy & Sell Website'
admin.site.index_title='ABC Buying'

#para hacer que el admin sepa que campos se pueden editar
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','desc')
    #aca ponemos que cambo se quiere buscar en este caso el nombre
    search_fields=('name',)

    #con esto podemos definir nuestras propias acciones
    #customaction
    def set_price_to_zero(self,request,queryset):
        queryset.update(price=0)
    
    actions = ('set_price_to_zero',)
    #de esta manera los podemos hacer editables sin entrar al mismo producto desde el admin
    list_editable=('price','desc')


admin.site.register(Product,ProductAdmin)