from django.db import models
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=200)
    BookingDate = models.DateTimeField(default=timezone.now)
    no_of_guests = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=10,decimal_places=2) 
   inventory = models.IntegerField(max_length=5,default=0) 

   def __str__(self):
      return self.name