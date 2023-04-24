from django.db import models
from datetime import date

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=254, null=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_content = models.TextField()
    publication_date = models.DateField(default=date.today)

    def __str__(self):
        return self.headline
