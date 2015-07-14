from django.db import models

#Country
class Country(models.Model):
	class Meta:
		verbose_name_plural = "Countries"

	name = models.CharField(max_length=100)
	prefix = models.CharField(max_length=100, blank=True, null=True, default=None)
	active = models.BooleanField(default=True, db_index=True)
	
	def __unicode__(self):
		return self.name

	def to_object(self):
		return {
			'name' : self.name
		}

#State
class State(models.Model):
	class Meta:
		verbose_name_plural = "States"

	name = models.CharField(max_length=100)
	prefix = models.CharField(max_length=10, blank=True, null=True)
	active = models.BooleanField(default=True, db_index=True)
	
	def __unicode__(self):
		return self.name

	def to_object(self):
		return {
			'name' : self.name
		}


#City
class City(models.Model):
	class Meta:
		verbose_name_plural = "Cities"

	name = models.CharField(max_length=100)
	country = models.ForeignKey(Country)
	state = models.ForeignKey(State, blank=True, null=True)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name

	def to_object(self):
		return {
			'name' : self.name,
			'state' : unicode(self.state),
			'country' : unicode(self.country),
		}



#Locatio
class Location(models.Model):
	class Meta:
		verbose_name_plural = "Location"

	name = models.CharField(max_length=100, blank=True, null=True)
	city = models.ForeignKey(City)
	latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)
	longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name

	def to_object(self):
		return {
			'name' : unicode(self.name),
			'city' : unicode(self.city),
			'latitude' : self.latitude,
			'longitude' : self.longitude,
		}