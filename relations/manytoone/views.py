from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def create(request):
    rep1 = Reporter.objects.create(first_name = 'John', last_name = 'DiMarco', email = 'john@example.com')
    rep2 = Reporter.objects.create(first_name = 'Louis', last_name = 'Stephan', email = 'louis@example.com')


    art1 = Article.objects.create(headline = 'Demo article', pub_date=date(2026,6,28), reporter = rep1)
    art2 = Article.objects.create(headline = 'Lorem Ipsum', pub_date=date(2026,7,4), reporter = rep1)
    art3 = Article.objects.create(headline = 'Dogs, cats and more', pub_date=date(2026,7,20), reporter = rep1)
    art4 = Article.objects.create(headline = 'Criptos', pub_date=date(2027,1,1), reporter = rep1)
    art5 = Article.objects.create(headline = 'Technology', pub_date=date(2024,3,12), reporter = rep2)
    art6 = Article.objects.create(headline = 'Space x', pub_date=date(2024,4,10), reporter = rep2)

    # Get from article to reporter
    # result = art1.reporter.first_name + ' | ' + art1.headline

    # Get from reporter to article
    # result = rep2.article_set.all()

    # And any type of filtering, like a normal query
    result = rep2.article_set.filter(headline__iexact='technology')

    return HttpResponse(result)
