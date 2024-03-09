from django.http import HttpResponse
from django.template import loader
from .models import Company


def indexone(request):
  template = loader.get_template('index.html')
  x = Company.objects.all().order_by('first_name').values()
  return HttpResponse(template.render({"y":x}, request))             