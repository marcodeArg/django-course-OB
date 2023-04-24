from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Article(models.Model):
    headline = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline