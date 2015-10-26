from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from random import choice
from string import ascii_lowercase, digits
from members.models import *
from locations.models import *
import json

class MembersUtils:

	@classmethod
	def generate_random_username(self, length=16, chars=ascii_lowercase+digits, split=4, delimiter='-'):
		username = ''.join([choice(chars) for i in xrange(length)])
		if split:
			username = delimiter.join([username[start:start+split] for start in range(0, len(username), split)])
		try:
			User.objects.get(username=username)
			return self.generate_random_username(length=length, chars=chars, split=split, delimiter=delimiter)
		except User.DoesNotExist:
			return username;



	@classmethod
	def create_user(self, email):
		return User.objects.create_user(self.generate_random_username(), email, User.objects.make_random_password())



	@classmethod
	def handle_save_response(self, member, request):
		error = None
		if request.body and request.method == 'PUT':
			try:
				member_body = json.loads(request.body)
				if member_body['user']:
					if member_body['user']['email']:
						if not member.user:
							user = self.create_user(member_body['user']['email'])
							member.user = user
							member.save()
			except ValueError, e:
				error = e
		return member, error



	@classmethod
	def save_location_from_request(self, request):
		if not request.body:
			return None
		location_object = json.loads(request.body)
		location = None
		if "country" in location_object and "city" in location_object:
			try:
				country = Country.objects.get(name=location_object["country"])	
			except Country.DoesNotExist:
				country = Country()
				country.name = location_object["country"]
				country.save()
			try:
				city = City.objects.get(name=location_object["city"])	
			except City.DoesNotExist:
				city = City()
				city.country = country
				city.name = location_object["city"]
				city.save()

			if "latitude" in location_object and "longitude" in location_object:
				try:
					location = Location.objects.get(latitude=location_object["latitude"], longitude=location_object["longitude"])	
				except Location.DoesNotExist:
					location = Location()
				location.city = city
				location.latitude = location_object["latitude"]
				location.longitude = location_object["longitude"]
				location.save()
		return location



	#Centralizes the user creation, the request for this function should contain a body as a json with the 
	#following format {"email":"bipsa81@gmail.com", "password":"123abc", "first_name":"Sebastian", "last_name":"Romero"}
	#The password is not required, if the request is sent without a password, prowlist will create one for the user
	#The firstname and lastname fields are not required also.
	@classmethod
	def create_prowlist_user(self, request):
		error = None
		user = None
		user_object = json.loads(request.body)
		try:
			user = User.objects.get(username=user_object["email"][:20])
			error = {
				"cod" : 103,
				"message" : "The user already exists."}		
		except User.DoesNotExist:
			if "password" in user_object:
				user_object["password"] = User.objects.make_random_password()
			user = User.objects.create_user(user_object["email"][:20], user_object["email"], user_object["password"])
			if "first_name" in user_object: 
				user.first_name = user_object["first_name"]
			if "last_name" in user_object: 
				user.last_name = user_object["last_name"]
			user.save()
		return user, error


	@classmethod	
	def get_member_with_token(self, token):
		member = None;
		error = None;
		try:
			token = Token.objects.get(token=token)
			try:
				error = None
				member = Member.objects.get(token=token)
			except Member.DoesNotExist:
				member = None
				error = {
					"cod" : 102,
					"message" : "The member was not found."}
		except Token.DoesNotExist:
			member = None
			error = {
				"cod" : 101,
				"message" : "The token provided is not valid."}
		return member, error



	#This method gets the memeber from request, if this returns an error means that the memeber 
	#was not found, returns the member if everuthing is correct.
	@classmethod
	def get_member_from_request(self, request):
		error = None
		member = None
		if 'HTTP_PROWLIST_USER' in request.META:
			member, error = self.get_member_with_token(request.META['HTTP_PROWLIST_USER'])
		elif 'prowlist-user' in request.GET:
			member, error = self.get_member_with_token(request.GET['prowlist-user'])
		else :
			error = {
				"cod" : 100,
				"message" : "No session provided."}
		return member, error

