from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html', {})

def dinamic(request, name):
    greetings = ['Hi', 'Hola', 'Ola', 'Priviet']
    context = {'name':name, 'greetings':greetings}
    return render(request, 'dinamic.html', context)