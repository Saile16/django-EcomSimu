from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def register(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, "Registration successful." )
            print('hello')
            return redirect('/myapp/products/')            
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context={'form':form}
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')

def create_profile(request):
    if request.method=='POST':
        contact_number= request.POST.get('contact_number')
        image=request.FILES['upload']
        #aqui pedimos el usuario afiliado a esta cuenta
        user=request.user
        profile=Profile(user=user,image=image,contact_number=contact_number)
        profile.save()    

    return render(request,'users/createprofile.html')