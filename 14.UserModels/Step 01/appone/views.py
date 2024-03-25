from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def Home(request):
    return render (request,'home.html')

def Signup(request):
   return render (request,'signup.html')

def Login(request):
  return render (request,'login.html')

def Logout(request):
   return redirect('login')