# Generated by Django 4.2.7 on 2023-11-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmbulanceApp', '0013_alter_products_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='Status',
            field=models.CharField(choices=[('Available', 'Active'), ('Unavailable', 'Inactive')], max_length=50),
        ),
    ]