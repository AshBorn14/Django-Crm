from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()


    #check to see if user is loggging in
    if request.method == "POST":
        us = request.POST['username']
        passwd = request.POST['password']
        #authenticate
        user = authenticate(request,username=us,password=passwd)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"Cannot log in try again")
            return redirect('home')
    else:
        return render(request,'index.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully been registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        #look up records
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be logged in to see records")
        return redirect('home')
    

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_user = Record.objects.get(id=pk)
        delete_user.delete()
        messages.success(request,"Record has been Successfully deleted")
        return redirect('home')
    else:
        messages.success(request,"You must log in to delete a record")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record has been added Successfully")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to add Record")
        return redirect('home')
    

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been successfully updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in order to Update Record")
        return redirect('home')
