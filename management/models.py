from django.db import models

from core.models import BaseModel

# Create your models here.

class Parking(BaseModel):
    PARKING_SPACE_CHOICES = [
        ('CONVENTIONAL', 'Convencional'),
        ('PRIORITY', 'Prioritária'),
    ]

    parking_name = models.CharField(max_length=100, default="Untitled Parking")
    hour_price = models.FloatField()
    num_spaces = models.IntegerField(default=0)
    space_type = models.CharField(max_length=20, choices=PARKING_SPACE_CHOICES,  default='Convencional')
    class Meta:
        verbose_name = "Parking"
        verbose_name_plural = "Parking Lots"

    def __str__(self) -> str:
        return f'{self.parking_name} - Price: {self.hour_price}'

class ParkingSpace(BaseModel):
    cod = models.CharField(max_length=10)
    status = models.BooleanField(default=False) 
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="spaces", null=True, default=None)

    class Meta:
        verbose_name = "Parking Space"
        verbose_name_plural = "Parking Spaces"
    
    def __str__(self) -> str:
        return f'{self.cod} | {self.parking} | Status: {self.status}'

class Ticket(BaseModel):
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    checkin = models.TimeField()
    checkout = models.TimeField()
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE, null=True, default=None)
    value = models.FloatField()

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self) -> str:
        return f'{self.id} | {self.model} | {self.license_plate} | {self.value}'

class Reservation(models.Model):
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # Se necessário, adicione mais campos para representar informações adicionais sobre a reserva

    def __str__(self):
        return f"Reservation for Parking Space {self.parking_space.cod}"