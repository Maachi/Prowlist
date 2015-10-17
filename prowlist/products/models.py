from datetime import datetime
from django.db import models
from locations.models import *
from tags.models import *


class Choise(models.Model):
	class Meta:
		verbose_name_plural = "Variant choises"

	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=20, decimal_places=2)

	def __unicode__(self):
		return self.name


#A product could have different variants this model represents a variant with a single choise
#An example could be Internet packages where the variants will be the different transfer speed or 
class Variant(models.Model):
	class Meta:
		verbose_name_plural = "Product variants"

	name = models.CharField(max_length=200)
	choise = models.ForeignKey(Choise)

	def __unicode__(self):
		return self.name



def upload_header_image(instance, filename):
	name, extension = os.path.splitext(filename)
	return os.path.join("uploads/products/%s/" % instance.pk, filename)


#This model defines a provider for the product, if the product has providers, the application will send a notification
class Provider(models.Model):
	class Meta:
		verbose_name_plural = "Products - Providers"

	name = models.CharField(max_length=200)
	point_contact_provider = models.CharField(max_length=200, blank=True, null=True, default=None)
	point_contact_email = models.CharField(max_length=200, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	locations = models.ManyToManyField(Location, blank=True)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name

	def serialize(self):
		return {
			'name' : self.name,
			'point_contact_provider' : self.point_contact_provider,
			'point_contact_email' : self.point_contact_email,
			'description' : self.description,
		}


#Defines the product structure
class Product(models.Model):
	class Meta:
		verbose_name_plural = "Products"

	name = models.CharField(max_length=200)
	variants = models.ManyToManyField(Variant, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	provider = models.ForeignKey(Provider, blank=True, null=True)
	description = models.TextField(blank=True, null=True, default=None)
	header_image = models.FileField(upload_to=upload_header_image, blank=True, null=True, default=None)
	active = models.BooleanField(default=True, db_index=True)

	
	def __unicode__(self):
		return self.name

	def serialize(self):
		tags = []
		provider = {}
		header_image = None
		if self.header_image:
			header_image = self.header_image.url
		if self.provider:
			provider = self.provider.serialize()
		for tag in self.tags.all():
			tags.append(tag.to_object())
		return {
			'id' : self.pk,
			'name' : self.name,
			'tags' : tags,
			'header_image' : header_image,
			'description' : self.description,
			'provider' : provider
		}
