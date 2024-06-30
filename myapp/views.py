from django.shortcuts import render,redirect
from .models import information
from .forms import Signup_Form,Login_Form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def getform(request):
    if request.method=="POST":
        username = request.Post["username"]
        email = request.Post["email"]
        age = request.Post["age"]
        information(username = username, email=email, age=age).save()
        return redirect("/")
    return render(request,"form.html")

def getdata(request):
    data = information.objects.all()
    print(data)
    context = {
        'mydata' : data
    }
    return render(request,"data.html",context)

def update(request,id):
    data = information.objects.filter(id=id)
    if request.method=='POST':
        data.username = request.Post["username"]
        data.email = request.Post["email"]
        data.age = request.Post["age"]
        data.save()
        return redirect("/")
    print(data)
    context ={
        'data' : data
    }
    return render(request,"update.html",context)

def delete(request, id):
    data = information.objects.get(id=id)
    data.delete()
    return redirect('/data/')

def signup(request):
    if request.method=="POST":
        form = Signup_Form(request.POST)
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        if User.objects.filter(username=username).first():
            messages.success(request, "This username is already taken")
        elif User.objects.filter(email=email).first():
            messages.success(request, "This email is already taken")
        elif password != confirm_password:
            messages.success(request,"Both password foeld should be same")
        else:
            user= User(username=username, email=email)
            user.setpassword(password)
            user.save()
            messages.success(request,"Account successfully created")
            return redirect('/signup/')
    form = Signup_Form()
    context = {
        'form' : form
    }
    return render(request,"signup.html", context)

def login(request):
    form = Login_Form(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data['password']
        
        user = authenticate(userename=username , password=password)
        if user is not None():
            login(request,user)
            return redirect('/')
        else:
            messages.success(request,"Wrong Password")
    form = Login_Form()
    return render(request,'login.html',{'form': form})

def logout(request):
    logout(request)
    return redirect('/login/')



        
