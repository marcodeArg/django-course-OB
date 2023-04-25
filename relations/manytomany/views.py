from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

# Create your views here.
def create(request):
    pub1 = Publication.objects.create(title='Publication one')
    pub2 = Publication.objects.create(title='Publication two')
    pub3 = Publication.objects.create(title='Publication three')
    pub4 = Publication.objects.create(title='Publication four')
    pub5 = Publication.objects.create(title='Publication five')
    pub6 = Publication.objects.create(title='Publication six')
    pub7 = Publication.objects.create(title='Publication seven')


    art1 = Article.objects.create(headline='Article one')
    art2 = Article.objects.create(headline='Article two')
    art3 = Article.objects.create(headline='Article three')

    art1.publications.add(pub1)
    art1.publications.add(pub4)
    art1.publications.add(pub6)
    art2.publications.add(pub2)
    art2.publications.add(pub7)
    art3.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub1)

    result = art1.publications.all()

    return HttpResponse(result)
