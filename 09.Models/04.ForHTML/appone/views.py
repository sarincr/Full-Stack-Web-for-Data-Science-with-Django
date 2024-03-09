from django.http import HttpResponse
from django.template import loader
from .models import Company


def indexone(request):
  template = loader.get_template('index.html')
  X = Company.objects.all().values()
  return HttpResponse(template.render({"y":X}, request))             