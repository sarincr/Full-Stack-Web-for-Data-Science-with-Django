from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")


def aboutus(request):
    return HttpResponse("Hello User")