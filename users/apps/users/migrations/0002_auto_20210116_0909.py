# Generated by Django 3.1.5 on 2021-01-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_names',
            field=models.CharField(blank=True, max_length=30, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='names',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nombres'),
        ),
    ]
