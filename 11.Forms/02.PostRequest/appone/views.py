from django.shortcuts import render
from .models import Company

def indexone(request):
    if request.method=="POST":
        post=Company()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.phone=request.POST['phone']
        post.address=request.POST['address']
        post.save()
        return render(request, 'Index.html')
    else:
        return render(request, 'Index.html')