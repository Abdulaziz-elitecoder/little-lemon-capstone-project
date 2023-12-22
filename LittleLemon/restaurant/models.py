from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.name} - {self.booking_date.date()}"
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'