# Generated by Django 3.2.6 on 2021-09-08 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_drivers_wins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='age',
            field=models.IntegerField(default=18, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='nationality',
            field=models.CharField(choices=[('United Kingdom', 'United Kingdom'), ('Spain', 'Spain'), ('Netherlands', 'Netherlands'), ('Belgium', 'Belgium '), ('Germany', 'Germany'), ('United States', 'United States'), ('Brasil', 'Brasil '), ('Japan', 'Japan'), ('Australia', 'Australia')], max_length=255),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='summarry',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='wins',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)]),
        ),
    ]