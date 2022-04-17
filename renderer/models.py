from datetime import date
from django.db import models

class Detector(models.Model):
    x_coord = models.FloatField(blank=False)
    y_coord = models.FloatField(blank=False)

    def __str__(self):
        return self.pk

class Anomaly(models.Model):
    center_x = models.FloatField()
    center_y = models.FloatField()

    def __str__(self):
        return self.pk

class DetectAnomaly(models.Model):
    detector_id = models.ForeignKey(Detector, on_delete=models.CASCADE)
    anomaly_id = models.ForeignKey(Anomaly, on_delete=models.CASCADE)
    rate = models.FloatField(blank=False)   

    def __str__(self):
        return self.pk



