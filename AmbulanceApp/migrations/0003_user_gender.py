# Generated by Django 4.2.7 on 2023-11-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmbulanceApp', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]
