from django.db import models

# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=100)
    weight = models.IntegerField()
    frequency = models.IntegerField()