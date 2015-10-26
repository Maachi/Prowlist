from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from datetime import datetime
from django.db import models
from locations.models import *
import hashlib
import os


def upload_photo_to(instance, filename):
	return os.path.join("uploads/members/profile/%s" % instance.id, filename)


def upload_avatar_to(instance, filename):
	return os.path.join("uploads/avatars/", filename)


class Avatar (models.Model):
	class Meta:
		verbose_name_plural = "Avatars - Prowlist user Avatars"

	image = models.ImageField(upload_to=upload_avatar_to, blank=True, null=True, default=None)

	def __unicode__(self):
		return unicode(self.id)


#This model represents the user profile use this class to extend user data
class Profile(models.Model):
	
	class Meta:
		verbose_name_plural = "Profile - Prowlist user Profile"

	gender = models.CharField(max_length=32, choices=[
		("1", "Male"),
		("2", "Female")
	], default=None, blank=True, null=True)
	photo = models.ImageField(upload_to=upload_photo_to, blank=True, null=True, default=None)
	avatar = models.ImageField(upload_to=upload_photo_to, blank=True, null=True, default=None)
	birth_date = models.DateField(blank=True, null=True)


	def __unicode__(self):
		return unicode(self.id)

	def to_object(self):
		photo = None
		avatar = None
		if self.photo:
			image = get_thumbnail(self.photo, '400x400', crop='center', quality=99)
			photo = image.url
		if self.avatar:
			avatar = self.avatar.url
		else:
			try :
				image_avatar = Avatar.objects.order_by('?').first()
				if image_avatar:
					avatar = get_thumbnail(image_avatar.image, '400x400', crop='center', quality=99).url
			except Avatar.DoesNotExist:
				avatar = None
		return {
			"avatar" : avatar,
			"photo" : photo,
			"gender" : self.gender,
			"birth_date" : self.birth_date
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
	devices = models.ManyToManyField(Device, blank=True)

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

	token = models.OneToOneField(Token)
	user = models.OneToOneField(User, blank=True, null=True) #Supports anonymous users
	cell_phone = models.CharField(max_length=250, blank=True, null=True)
	profile = models.OneToOneField(Profile, blank=True, null=True)
	friends = models.ManyToManyField('self', blank=True)
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
		last_location = None
		profile = None
		if self.profile:
			profile = self.profile.to_object()
		else:
			member_profile = Profile()
			member_profile.save()
			self.profile = member_profile
			self.save()
			profile = self.profile.to_object()
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
			"profile" : profile,
			"last_location" : last_location
		}

