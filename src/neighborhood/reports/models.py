from django.db import models

class Report(models.Model):
    name = models.CharField('Zgloszenie',max_length=200)
    value = models.IntegerField('Plusy')
    location = models.CharField('Lokalizacja',max_length=200)
# Create your models here.
