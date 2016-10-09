from datetime import datetime
from django.db import models

#Sensor
class Sensor(models.Model):
    class Meta:
        verbose_name_plural = "Sensors (Proximity detectors)"

    name = models.CharField(max_length=200)
    uuid = models.CharField(max_length=250, default=None, blank=True, null=True)
    serial = models.CharField(max_length=250, default=None, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)
    active = models.BooleanField(default=True, db_index=True)
    
    def __unicode__(self):
        return self.name

    def to_object(self):
        return {
            'name' : self.name,
            'uuid' : self.uuid,
            'serial' : self.serial,
            'latitude' : self.latitude,
            'longitude' : self.longitude,
        }



class SensorLogs(models.Model):
    class Meta:
        verbose_name_plural = "Sensor Logs"

    message = models.CharField(max_length=200)
    sensor = models.ForeignKey(Sensor, blank=True, null=True)
    validated_email_date = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

    def to_object(self):
        return {
            'name' : self.name
        }