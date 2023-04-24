from django.shortcuts import render
from .models import Author, Post
from django.http import HttpResponse

# Create your views here.
def queries(request):
    # Get all the author 
    authors = Author.objects.all()

    # Get an author using a filter (return a list)
    filtered = Author.objects.filter(email = "olivia19@example.org")
    
    # Get an author using a filter (return a element)
    author = Author.objects.get(id=1)

    # Set a limit
    limited_data = Author.objects.all()[9:19]

    # Order by
    ordered_data = Author.objects.order_by('email')

    # Data lowwer and equal than... (__lte (lower than equals))
    filtered2 = Author.objects.filter(id__lte=15)
    return render(request, 'posts/queries.html', {"authors": authors, "filtered": filtered, "author": author, "limit":limited_data, "order_data": ordered_data, "filtered2": filtered2})

def update(request):
    author = Author.objects.get(id=4)
    author.name = 'mrc'
    author.email = 'mrc@example.org'
    author.save()
    return HttpResponse('Updated!')