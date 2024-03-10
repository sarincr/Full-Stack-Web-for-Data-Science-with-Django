from django.http import HttpResponse
from django.template import loader
from .models import Company
from .forms import CustomerForm
from django.shortcuts import render

def indexone(request):
    form = CustomerForm()

    if request.method == 'POST':
      form = CustomerForm(request.POST)
      if form.is_valid():
        form.save()
        
    context = {'x':form}
    return render(request, 'index.html', context)   