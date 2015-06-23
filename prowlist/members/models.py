from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
import os

#This contains the authorizations token for the user 
class Token(models.Model):
	
	class Meta:
		verbose_name_plural = "Members - Tokens or Sessions"

	token = models.CharField(max_length=250, blank=True, null=True)
	user = models.ForeignKey(User)
	client = models.TextField(blank=True, null=True)
	date = models.DateTimeField(default=datetime.now())

	@staticmethod
	def get_user_by_token(token):
		try:
			token_object = Token.objects.get(token=token)
			return token_object.user
		except Token.DoesNotExist:
			return None

	def get_token(self, user):
		return default_token_generator.make_token(user)

	#Generates the token for the session
	def generate(self):
		if not self.token :
			self.token = self.get_token(self.user)
			self.save()

	def check_token(self):
		return default_token_generator.check_token(self.user, self.token)

	def __unicode__(self):
		return unicode(self.user)


def upload_photo_to(self, instance, filename):
	return os.path.join("uploads/members/profile/%s" % instance.id, filename)


#This model represents the user profile use this class to extend user data
class Profile(models.Model):
	
	class Meta:
		verbose_name_plural = "Members - Prowlist user Profile"

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


#Members
class Member(models.Model):
	
	class Meta:
		verbose_name_plural = "Members - Prowlist Application Users"

	user = models.ForeignKey(User, blank=True, null=True) #Supports anonymous users
	cell_phone = models.CharField(max_length=250, blank=True, null=True)
	profile = models.ForeignKey(Profile, blank=True, null=True)
	friends = models.ManyToManyField('self', blank=True, null=True)
	terms_agreed = models.BooleanField(default=True, db_index=True)
	active = models.BooleanField(default=True, db_index=True)
	validated_email = models.BooleanField(default=False, db_index=True)
	validated_email_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	validated_cell_phone_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __unicode__(self):
		return unicode(self.user)
