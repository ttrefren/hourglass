from django.db import models

from timekeeper.task.models import Type
# Create your models here.

class Task(models.Model):
    start = models.DateTimeField()
    task = models.TextField()
    task_type = models.ForeignKey(Type)
    end = models.DateTimeField(blank=True, null=True)
