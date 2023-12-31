# Generated by Django 4.2.7 on 2023-11-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmbulanceApp', '0010_rename_ambulancenumber_ambulance_ambulance_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('origin', models.CharField(default='Kenya', max_length=50)),
                ('color', models.CharField(default='White', max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]
