from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    stock = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return self.title