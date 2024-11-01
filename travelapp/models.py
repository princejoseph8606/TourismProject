from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    USER_TYPES = (('vendor', 'Vendor'), ('user', 'User'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    mobile_number = models.CharField(max_length=15, unique=True)

class TravelPackage(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    max_number_of_persons = models.IntegerField()
    hotel_type = models.CharField(max_length=50)
    food_type = models.CharField(max_length=50)
    number_of_days = models.IntegerField()
    number_of_nights = models.IntegerField()
    visiting_places = models.TextField()
    description = models.TextField()
    tour_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    image1 = models.ImageField(upload_to='packages/', null=True, blank=True)
    image2 = models.ImageField(upload_to='packages/', null=True, blank=True)
    image3 = models.ImageField(upload_to='packages/', null=True, blank=True)

    def is_expired(self):
        return self.tour_date < timezone.now().date()



