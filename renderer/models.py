from datetime import date
from django.db import models

class Detector(models.Model):
    id = models.IntegerField(primary_key=True)
    x_coord = models.FloatField(null=False)
    y_coord = models.FloatField(null=False)

    def __str__(self):
        return str(self.id)

class Anomaly(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    center_x = models.FloatField(null=True)
    center_y = models.FloatField(null=True)
    real_rate = models.FloatField(null=True)

    def __str__(self):
        return str(self.id)

class DetectAnomaly(models.Model):
    detector_id = models.ForeignKey(Detector, on_delete=models.CASCADE)
    anomaly_id = models.ForeignKey(Anomaly, on_delete=models.CASCADE)
    rate = models.FloatField(blank=False)   

    def __str__(self):
        return self.pk



