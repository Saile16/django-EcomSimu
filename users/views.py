from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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