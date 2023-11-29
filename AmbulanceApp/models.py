from django.db import models


# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=15)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Ambulance(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    AMBULANCE_TYPE = [
        ('Basic', 'Basic Life Support Ambulance'),
        ('Advance', 'Advance Life Support Ambulance'),
        ('Patient', 'Patient Transfer Ambulance'),
        ('Mortuary', 'Mortuary Ambulance'),
    ]
    STATUS = [
        ('Active', 'Available'),
        ('Inactive', 'Unavailable'),
    ]
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    Ambulance_No = models.CharField(max_length=14)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=15)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    Ambulance_type = models.CharField(max_length=50, choices=AMBULANCE_TYPE)
    Status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.firstname + " " + self.lastname
