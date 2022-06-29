from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    pages = models.IntegerField(default=1000)

    def __str__(self):
        return self.name
