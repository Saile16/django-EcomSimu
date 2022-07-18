from itertools import product
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
#para crear algo en la db se usa
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return HttpResponse('Hello World')

#con esto listamos los productos en el home o index de la app usando funciones
def products(request):
    page_obj=products=Product.objects.all()
    #obtenemos el product_name para el search de productos
    product_name=request.GET.get('product_name')    
    if product_name!='' and product_name is not None:
        page_obj=products.filter(name__icontains=product_name)
    #hacer pagination con function vviews
    paginator=Paginator(page_obj,3)
    #usamos normalmente el products pero lo cambiamos a page_obj para poder usar
    #la functionalidad de search
    # paginator=Paginator(products,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    # context={'products':products} 
    context={'page_obj':page_obj}
    return render(request,'myapp/index.html',context)
    
#Class Base view for abovce products view ListView
#con esto listamos los productos de la app usando clases los cambios se hacen tambien
# en el archivo urls.py
class ProductListView(ListView):
    model=Product
    template_name='myapp/index.html'
    context_object_name='products'
    paginate_by=3

def product_detail(request,id):
    product_detail=Product.objects.get(id=id)
    context={'product_detail':product_detail}
    return render(request,'myapp/detail.html',context)

#class base view for detail product
class ProductDetailView(DetailView):
    model=Product
    template_name='myapp/detail.html'
    context_object_name='product_detail'
    
@login_required
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        image=request.FILES['upload']
        seller_name=request.user
        product = Product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)        
        product.save()
    return render(request,'myapp/addproduct.html')

#de esta manera estamos creando una vista para crear un producto cuando lo hacemos de eta manera
#la clase busca el template llamado product_form.html tenemos que crearlo
class ProductCreateView(CreateView):
    model=Product
    fields=['name','price','desc','image','seller_name']
    

def update_product(request,id):
    product_edit=Product.objects.get(id=id)
    if request.method=='POST':
        product_edit.name=request.POST.get('name')
        product_edit.price=request.POST.get('price')
        product_edit.desc=request.POST.get('desc')
        product_edit.image=request.FILES['upload']
        product_edit.save()
        return redirect('/myapp/products/')
    context={'product_edit':product_edit}
    return render(request,'myapp/updateproduct.html',context)

class ProductUpdateView(UpdateView):
    model=Product
    fields=['name','price','desc','image','seller_name']
    template_name_suffix='_update_form'
    #al ahcer el update redirigimos al usuario a la pagina de productos
    #eso se hace en el archivo de models.py
    

def delete_product(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    if request.method=='POST':
        product.delete()
        return redirect('/myapp/products/')
    return render(request,'myapp/delete.html',context)

#classview delete
class ProductDelete(DeleteView):
    model=Product
    success_url=reverse_lazy('myapp:products')

def my_listing(request):
    #aca buscamos los productos que pertenecen a este usuario(request.user)
    products=Product.objects.filter(seller_name=request.user)
    context={'products':products}
    return render(request,'myapp/mylisting.html',context)