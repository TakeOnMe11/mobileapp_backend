from django.db import models
from datetime import datetime


class Sets(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)


class MeasTypes(models.Model):
    description = models.CharField(max_length=400)


class Results(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    measdate = models.DateTimeField(default=datetime.now())
    setid = models.ForeignKey(Sets, on_delete=models.PROTECT)
    typeid = models.ForeignKey(MeasTypes, on_delete=models.PROTECT)
    comment = models.CharField(max_length=600)
    data = models.TextField()
