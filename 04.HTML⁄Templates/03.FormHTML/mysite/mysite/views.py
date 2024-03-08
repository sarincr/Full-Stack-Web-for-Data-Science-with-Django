from django.http import HttpResponse
from django.shortcuts import render







def index(request):
    itemsidct = {"Name": "John", "Dept":"HR", "Age":22}
    return render(request, 'index.html', itemsidct)