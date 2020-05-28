from djgeojson.fields import PolygonField
from django.db import models


# Create your models here.
class Point(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
