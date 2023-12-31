# Generated by Django 4.2.7 on 2023-11-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmbulanceApp', '0007_rename_firstname_ambulance_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ambulance',
            old_name='ambulanceNumber',
            new_name='ambulance_number',
        ),
        migrations.RenameField(
            model_name='ambulance',
            old_name='ambulanceStatus',
            new_name='ambulance_status',
        ),
        migrations.RenameField(
            model_name='ambulance',
            old_name='ambulanceType',
            new_name='ambulance_type',
        ),
        migrations.RenameField(
            model_name='ambulance',
            old_name='emailAddress',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='ambulance',
            old_name='FirstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='ambulance',
            old_name='LastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='ambulance',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='ambulance',
            old_name='driverPassword',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='ambulance',
            name='userName',
        ),
        migrations.AddField(
            model_name='ambulance',
            name='driver_password',
            field=models.CharField(default='exit', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
