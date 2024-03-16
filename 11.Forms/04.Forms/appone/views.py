from django.shortcuts import render


def indexone(request):
    return render(request,"home.html")


def result(request):
    a= request.GET["x"]
    b= request.GET["y"]
    z= a+" "+b
    return render(request,"results.html",{"res":z})