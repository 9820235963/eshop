from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def homePage(request):
    return render(request, 'index.html')


def shop(request):
    ProductDetails = Product.objects.all()
    context = {"ProductDB": ProductDetails}
    return render(request, 'shop.html', context)

def base(request):
    return render(request, 'base.html',)

def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    return render(request, 'login.html',)

def register(request):
    if request.method=="POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password")

        if(password!=confirm_password):
            messages.error(request,"password doesn't match")
            return render(request,'register.html')
        
        elif(len(password)):
            messages.error(request,"Your password length is less than 8 char.")
        
        user = User.objects.create_user(
    username=username,
    password=password,
    email=email,
    first_name=firstname,
    last_name=lastname
)
        user.set_password(password)
        user.save()
    return render(request,'register.html')