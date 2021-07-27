from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from mapbox_location_field.models import LocationField
import datetime
import uuid

from django.contrib.postgres.fields import ArrayField






# Create your models here.
class User(models.Model):
    status_choices = (
        ("A","Active"),
        ("I","Inactive")
    )
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=500)
    
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")
    status = models.CharField(max_length=1, choices = status_choices)

    def __str__(self):
        return "{} -{} -{}".format(self.first_name, self.last_name, self.email)


class ServiceProvider(models.Model):

    status_choices = (
        ("A","Active"),
        ("I","Inactive")
    )

    sp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    location = LocationField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    status = models.CharField(max_length=1, choices = status_choices)
    ratings = models.DecimalField(max_digits=9, decimal_places=6)


class Trucks(models.Model):
    truck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    truck_image = models.ImageField()



class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = LocationField()
    pickup_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_location = LocationField()
    dropoff_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_date = models.DateTimeField()
    serice_provider_id = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    serviceProviderTruck_id = models.ForeignKey(Trucks, on_delete=models.CASCADE)


class ServiceProviderUser(models.Model):
    serviceProviderUser_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sp_id = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)


class ServiceProviderTruck(models.Model):
    serviceProviderTruckId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    truck_id = models.ForeignKey(Trucks, on_delete=models.CASCADE)
    sp_id = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    estimate= models.DecimalField(max_digits=20, decimal_places=2)
    





