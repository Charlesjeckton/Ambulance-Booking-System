# Generated by Django 4.2.7 on 2023-11-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmbulanceApp', '0012_alter_ambulance_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
