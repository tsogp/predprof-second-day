from datetime import date
from django.db import models

class Anomaly(models.Model):
    name = models.CharField(max_length=200)
    rate = models.FloatField(blank=False)

    def __str__(self):
        return self.name

class Detector(models.Model):
    x_coord = models.FloatField(blank=False)
    y_coord = models.FloatField(blank=False)
    anomaly_id = models.ForeignKey(Anomaly, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pk

