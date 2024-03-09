from django.http import HttpResponse
from django.template import loader
from .models import Company


def indexone(request):
  template = loader.get_template('index.html')
  x = Company.objects.filter(id__range=(2, 4)).values()
  return HttpResponse(template.render({"y":x}, request))             