from django.shortcuts import render
from django.http import HttpResponse
from .forms import Comment, ContactForm

def form(request):
    comment_form = Comment()

    return render(request, 'form.html', {"comment_form": comment_form})

def goal(request):
    if request.method != "GET":
        return HttpResponse('There is not a post method available in this form')
    
    return HttpResponse(request.GET['name'])

def widget(request):
    if request.method == "GET":
        contact_form = ContactForm()
        return render(request, 'widget.html', {"contact_form": contact_form})

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            return HttpResponse('Welcome!')
        else:
            return render(request, 'widget.html', {"contact_form": contact_form})