from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
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
        return render(request,'index.html')

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})