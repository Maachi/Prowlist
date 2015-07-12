from locations.models import *
from products.models import *
from sensors.models import *
from themes.models import *
from tags.models import *
from datetime import datetime
from django.db import models


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


class Venue(models.Model):
	class Meta:
		verbose_name_plural = "Venues"

	name = models.CharField(max_length=200)
	brand = models.ForeignKey(Brand)
	location = models.ForeignKey(Location)
	small_description = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True, default=None)
	image = models.FileField(upload_to=upload_venue_image, blank=True, null=True, default=None)
	products = models.ManyToManyField(Product, blank=True)
	types = models.ManyToManyField(Type, blank=True)
	attributes = models.ManyToManyField(Attribute, blank=True)
	active = models.BooleanField(default=True, db_index=True)

	
	def __unicode__(self):
		return self.name

	def to_object(self):
		return {
			'name' : self.name
		}

