from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        try:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                # Username already exists, handle accordingly
                messages.error(request, "Username already exists. Please choose a different username.")
                return redirect('signup')
            
            # Username doesn't exist, create the user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your Account has been created successfully!! Please check your email to confirm your email address in order to activate your account.")
            return redirect('signin')
        
        except IntegrityError:
            # Handle IntegrityError
            messages.error(request, "An error occurred while creating your account. Please try again.")
            return redirect('signup')
               
    return render(request, "signup.html")



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "home.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')