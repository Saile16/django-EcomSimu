from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def products(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'myapp/index.html',context)
    

def product_detail(request,id):
    product_detail=Product.objects.get(id=id)
    context={'product_detail':product_detail}
    return render(request,'myapp/detail.html',context)

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




def delete_product(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    if request.method=='POST':
        product.delete()
        return redirect('/myapp/products/')
    return render(request,'myapp/delete.html',context)