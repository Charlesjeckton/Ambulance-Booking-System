# Generated by Django 4.2.7 on 2023-11-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmbulanceApp', '0004_ambulance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
