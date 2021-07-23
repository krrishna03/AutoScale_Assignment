from django.db import models

# Create your models here.

class Dealer(models.Model):
    dealer_number = models.IntegerField(default=0)
    dealer_name = models.CharField(max_length=200)
    dealer_address = models.CharField(max_length=200, null=True)

class Vehicle(models.Model):
    vehicle_live_id = models.IntegerField()
    vin = models.CharField(max_length=200)
    stock = models.CharField(max_length=200, null=True)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    trim = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.IntegerField(null=True)
    miles = models.IntegerField()
    exterior = models.CharField(max_length=200, null=True)
    description = models.TextField(default=000)
    certified = models.BooleanField()
    transmission = models.TextField(null=True)
    body_type = models.CharField(max_length=200)
    speeds = models.IntegerField(null=True)
    doors = models.IntegerField(null=True)
    cylinders = models.IntegerField(null=True)
    engine  = models.CharField(max_length=200, null=True)
    displacement = models.IntegerField(null=True)
    pincode = models.IntegerField(default=000000)
    phone = models.IntegerField(null=True)
    dealer_number = models.IntegerField()
    distance = models.IntegerField(null=True)


class ZipList(models.Model):
    pincode = models.IntegerField(default=00000)
    state_code = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=20,decimal_places=10)
    longitude = models.DecimalField(max_digits=20,decimal_places=10)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)




