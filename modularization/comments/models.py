from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=255, null=False, default='null')
    rating = models.IntegerField(default='3')
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.name