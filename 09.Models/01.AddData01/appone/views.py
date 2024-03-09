from django.http import HttpResponse
from django.template import loader

def theindex(request):
  template = loader.get_template('index.html')
  x= {
    'emp': ['John', 'Adam', 'Cherry'],   
  }
  return HttpResponse(template.render(x, request))                     