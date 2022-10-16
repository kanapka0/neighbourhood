# Generated by Django 4.1.2 on 2022-10-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Autor')),
                ('title', models.CharField(max_length=200, verbose_name='Tytul')),
                ('description', models.CharField(max_length=1000, verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Zgloszenie')),
                ('surname', models.CharField(max_length=200, verbose_name='Nazwisko')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('description', models.CharField(max_length=1000, verbose_name='Opis')),
                ('location', models.CharField(max_length=200, verbose_name='Lokalizacja')),
                ('done', models.BooleanField(verbose_name='Zrobione')),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.CharField(max_length=200, verbose_name='Lokalizacja'),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Zgloszenie'),
        ),
        migrations.AlterField(
            model_name='report',
            name='value',
            field=models.IntegerField(verbose_name='Plusy'),
        ),
    ]