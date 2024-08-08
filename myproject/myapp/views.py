from django.http import HttpResponse

def text(request):
    return HttpResponse("Hello wolrd")