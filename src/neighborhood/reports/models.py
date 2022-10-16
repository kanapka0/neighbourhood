from django.db import models

class Report(models.Model):
    name = models.CharField('Zgloszenie',max_length=200)
    value = models.IntegerField('Plusy')
    location = models.CharField('Lokalizacja',max_length=200)
# Create your models here.

class Submissions(models.Model):
    name = models.CharField('Zgloszenie', max_length=200)
    surname = models.CharField('Nazwisko',max_length=200)
    email = models.EmailField('Email',max_length=200)
    description = models.CharField('Opis',max_length=1000)
    location = models.CharField('Lokalizacja', max_length=200)
    done = models.BooleanField('Zrobione')


class Announcements(models.Model):
    name = models.CharField('Autor', max_length=200)
    title = models.CharField('Tytul',max_length=200)
    description = models.CharField('Opis', max_length=1000)


class NeighborlyHelp(models.Model):
    title = models.CharField('Tytul',max_length=200)
    name = models.CharField('Autor', max_length=200)
    description = models.CharField('Opis', max_length=1000)

class Comments(models.Model):
    comment = models.CharField('Komentarz', max_length=400)
    title = models.ForeignKey('NeighborlyHelp', on_delete=models.CASCADE , null=True)