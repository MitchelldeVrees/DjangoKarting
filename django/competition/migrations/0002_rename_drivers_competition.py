# Generated by Django 3.2.6 on 2021-09-08 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_auto_20210908_1303'),
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drivers',
            new_name='Competition',
        ),
    ]
