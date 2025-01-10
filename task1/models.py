from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=10, max_digits=11)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=10, max_digits=11)
    size = models.DecimalField(decimal_places=5, max_digits=6)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
