# Generated by Django 4.2.4 on 2023-09-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desafio',
            name='estimativa',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10, verbose_name='Estimativa de tempo em minutos'),
        ),
    ]
