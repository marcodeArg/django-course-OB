from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse("Working!")

def create(request):
    # First way, need to save() manually
    #comment = Comment(name="Marco", comment="Este es un comentario")
    #comment.save()

    # Second way, the save() is automatically called
    comment = Comment.objects.create(name="Juan")
    return HttpResponse("Creating")

def delete(request):
    # First way, need to delete() manually
    #comment = Comment.objects.get(id=2)
    #comment.delete()

    # Second way, the delete() is automatically called
    Comment.objects.filter(id=3).delete()
    return HttpResponse("Deleting")