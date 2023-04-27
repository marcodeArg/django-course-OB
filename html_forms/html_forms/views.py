from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="forms/">Forms</a>')


def getforms(request):
    return render(request, 'forms.html')

def getgoal(request):
    if request.method != 'GET':
      return HttpResponse('Oopss!')

    # Both options work perfectly
    #first_name = request.GET['first_name']

    form = request.GET
    first_name = form['first_name']
    return render(request, 'success.html', {'name': first_name})


def postforms(request):
    return render(request, 'postforms.html')


def postgoal(request):
    if request.method != 'POST':
        return HttpResponse('Oopss!')

    username = request.POST['user']
    return render(request, 'postsuccess.html', {'username': username})
    