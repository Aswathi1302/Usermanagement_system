from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request,'userapp/index.html', {
        'userapp': User.objects.all(),
    
    })
def view_user(request,id):
    user=User.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user_NO = form.cleaned_data['No']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_DOB = form.cleaned_data['DOB']
            new_address = form.cleaned_data['address']

            new_user = User(
                No=new_user_NO,
                first_name=new_first_name,
                last_name=new_last_name,
                DOB=new_DOB,
                address=new_address
            )
            new_user.save()
            return render(request, 'userapp/add.html', {
                'form': UserForm(),
                'success': True
            })
    else:
        form = UserForm()

    return render(request, 'userapp/add.html', {
        'form': UserForm()
    })

def edit(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'userapp/edit.html', {
                'form': form,
                'success': True
            })
    else:
        user = User.objects.get(pk=id)
        form = UserForm(instance=user)
    
    return render(request, 'userapp/edit.html', {
        'form': form
    })


def delete(request,id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()
    return HttpResponseRedirect(reverse('index'))    



  
    
             




            
            

         
    

