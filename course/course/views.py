from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World!")


def bye(reques):
    return HttpResponse("Good bye!")


def adult(request, age):
    if age >= 18:
        return HttpResponse("Adult")
    else:
        return HttpResponse("Younger")
