from django.http import HttpResponse
from django.template import loader
from .models import Company
from django.db.models import Q


def indexone(request):
  template = loader.get_template('index.html')
  x = Company.objects.filter(Q(first_name='John') | Q(address ='Texas')).values()
  return HttpResponse(template.render({"y":x}, request))             