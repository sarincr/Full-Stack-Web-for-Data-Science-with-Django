from django.http import HttpResponse
from django.shortcuts import render







def index(request):
    
    return render(request, 'index.html')


def empname(request):
    x=request.GET.get('abcd', 'default')
    print(x)
    return HttpResponse(x)