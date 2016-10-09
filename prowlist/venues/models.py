from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from locations.models import *
from products.models import *
from sensors.models import *
from themes.models import *
from tags.models import *
from datetime import datetime
from django.db import models
import os


def upload_logo_image(instance, filename):
    name, extension = os.path.splitext(filename)
    return os.path.join("uploads/venues/%s/logo/" % instance.pk, filename)


def upload_venue_image(instance, filename):
    name, extension = os.path.splitext(filename)
    return os.path.join("uploads/venues/%s/" % instance.pk, filename)


#All venues associates a brand that holds a company
class Brand(models.Model):
    class Meta:
        verbose_name_plural = "Venue Brand"

    name = models.CharField(max_length=200)
    logo = models.FileField(upload_to=upload_logo_image, blank=True, null=True, default=None)


#The attributes represents the differnt configuration that a product has
class Attribute (models.Model):
    class Meta:
        verbose_name_plural = "Venue Attributes"

    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    color = models.ForeignKey(Color)


class Type (models.Model):
    class Meta:
        verbose_name_plural = "Venue Types"

    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null=True, default=None)

    def to_object(self):
        return {
            'id' : self.pk,
            'key' : self.key,
        }


class Venue(models.Model):
    class Meta:
        verbose_name_plural = "Venues"

    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand)
    location = models.ForeignKey(Location)
    small_description = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, default=None)
    
    image = models.ImageField(upload_to=upload_venue_image, blank=True, null=True, default=None)

    products = models.ManyToManyField(Product, blank=True)
    types = models.ManyToManyField(Type, blank=True)
    attributes = models.ManyToManyField(Attribute, blank=True)
    products_count = models.IntegerField(blank=True, null=True)

    star_rating = models.IntegerField(blank=True, null=True)
    member_rating = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True, db_index=True)

    #Tagging for venues special for searching or segments
    tags = models.ManyToManyField(Tag, blank=True)
    sensors = models.ManyToManyField(Sensor, blank=True)

    height = models.IntegerField(default=120)
    tint = models.ForeignKey(Color, blank=True)
    controller_style = models.CharField(max_length=32, choices=[
        ("1", "ProwlistControllerStyleDefault"),
        ("2", "ProwlistControllerStyleLight")
    ], default=None, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, default=None)
    #Logo image
    logo_file = models.ImageField(upload_to=upload_venue_image, blank=True, null=True, default=None)


    def save(self, *args, **kwargs):
        if self.pk:
            if self.products.all():
                self.products_count = self.products.count()
        super(Venue, self).save(*args, **kwargs)

    
    def __unicode__(self):
        return self.name

    def serializeWithProducts(self):
        venue_serialized = self.serialize()
        products = []
        if self.products.all:
            for product in self.products.all():
                products.append(product.serialize())
        venue_serialized["products"] = products
        return venue_serialized

    def serialize(self):
        location = None
        image = None
        tint = None
        types = []
        tags = []
        sensors = []
        logo_file = None
        relative_path = None
        if self.tint:
            tint = self.tint.to_object()
        if self.location:
            location = self.location.to_object()
        if self.image:
            image = self.image.url
            relative_path = self.image.name
        if self.logo_file:
            logo_file = self.logo_file.url
        for type in self.types.all():
            types.append(type.to_object())
        for tag in self.tags.all():
            tags.append(tag.to_object())
        for sensor in self.sensors.all():
            if sensor.active:
                sensors.append(sensor.to_object())
        return {
            'id' : self.pk,
            'name' : self.name,
            'location' : location,
            'description' : self.description,
            'small_description' : self.small_description,
            'image' : image,
            'image_relative_path' : relative_path,
            'products_count' : self.products_count,
            'types' : types,
            'tags' : tags,
            'sensors' : sensors,
            'tint' : tint,
            'address' : self.address,
            'controller_style' : self.controller_style,
            'logo_file' : logo_file,
            'height' : self.height,
        }

