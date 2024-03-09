from django.http import HttpResponse
from django.template import loader
from .models import Company


def indexone(request):
  template = loader.get_template('index.html')
  x = Company.objects.all().values_list('first_name')
  return HttpResponse(template.render({"y":x}, request))             