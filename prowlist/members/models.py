from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from locations.models import *
import hashlib
import os


def upload_photo_to(instance, filename):
	return os.path.join("uploads/members/profile/%s" % instance.id, filename)


#This model represents the user profile use this class to extend user data
class Profile(models.Model):
	
	class Meta:
		verbose_name_plural = "Profile - Prowlist user Profile"

	gender = models.CharField(max_length=32, choices=[
		("1", "Male"),
		("2", "Female")
	], default=None, blank=True, null=True)
	photo = models.FileField(upload_to=upload_photo_to, blank=True, null=True, default=None)


	def __unicode__(self):
		return unicode(self.id)

	def to_object(self):
		photo = None
		if self.photo:
			photo = self.photo.url
		return {
			"photo" : photo,
			"gender" : self.gender,
		}


class Device(models.Model):

	class Meta:
		verbose_name_plural = "Devices - Session devices"


	client = models.TextField(blank=True, null=True)
	platform = models.CharField(max_length=250, blank=True, null=True)

	def __unicode__(self):
		return self.platform


#This contains the authorizations token for the user 
class Token(models.Model):
	
	class Meta:
		verbose_name_plural = "Token - Tokens or Sessions"

	token = models.CharField(max_length=250, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	devices = models.ManyToManyField(Device, blank=True, null=True)

	@staticmethod
	def get_user_by_token(token):
		try:
			token_object = Token.objects.get(token=token)
			return token_object.user
		except Token.DoesNotExist:
			return None

	def get_token(self):
		return hashlib.sha1(str(self.date)).hexdigest()

	#Generates the token for the session
	def generate(self):
		if not self.token :
			self.token = self.get_token()
			self.save()

	def __unicode__(self):
		return unicode(self.token)

	def save(self, *args, **kwargs):
		super(Token, self).save(*args, **kwargs)
		if not self.token:
			self.token = self.get_token()
			self.save()


#Members
class Member(models.Model):
	
	class Meta:
		verbose_name_plural = "Members - Prowlist Application Users"

	token = models.ForeignKey(Token)
	user = models.ForeignKey(User, blank=True, null=True) #Supports anonymous users
	cell_phone = models.CharField(max_length=250, blank=True, null=True)
	profile = models.ForeignKey(Profile, blank=True, null=True)
	friends = models.ManyToManyField('self', blank=True, null=True)
	terms_agreed = models.BooleanField(default=False, db_index=True)
	active = models.BooleanField(default=True, db_index=True)
	join_date = models.DateTimeField(blank=True, null=True)
	validated_email = models.BooleanField(default=False, db_index=True)
	validated_email_date = models.DateTimeField(blank=True, null=True)
	validated_cell_phone_date = models.DateTimeField(blank=True, null=True)

	locations = models.ManyToManyField(Location, blank=True)

	def __unicode__(self):
		label = unicode(self.token)
		return label

	def to_object(self):
		user = None
		last_location = None;
		if self.locations.all():
			last_location = self.locations.all()[0].to_object()
		if self.user :
			user = {
				"first_name" : self.user.first_name,
				"last_name" : self.user.last_name,
				"email" : self.user.email,
			}
		return {
			"token" : unicode(self.token),
			"user" : user,
			"last_location" : last_location
		}

