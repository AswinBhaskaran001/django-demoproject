from django.shortcuts import render,redirect
from shop.models import Category,Products
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def allcategories(request):
    k=Category.objects.all()
    return render(request,'category.html',{'b':k})

def allproduct(request,p):
    k=Category.objects.get(name=p)
    p=Products.objects.filter(category=k)
    return render(request,'product.html',{'k':k,'p':p})

def details(request,p):
    k=Products.objects.get(name=p)
    return render(request,'details.html',{'k':k})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        fname=request.POST['fname']
        lname=request.POST['lname']
        e=request.POST['e']



        if(p==p1):
            user=User.objects.create_user(username=u,password=p,first_name=fname,last_name=lname,email=e)
            user.save()
            return redirect('shop:allcategories')
        else:
            return HttpResponse("Password does not match")
    return render(request,"register.html")

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcategories')
        else:
            return HttpResponse("Invalid User")
    return render(request,"login.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:login')