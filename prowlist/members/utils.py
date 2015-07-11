from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from members.models import *
import json

class MembersUtils:


	#Centralizes the user creation, the request for this function should contain a body as a json with the 
	#following format {"email":"bipsa81@gmail.com", "password":"123abc", "first_name":"Sebastian", "last_name":"Romero"}
	#The password is not required, if the request is sent without a password, prowlist will create one for the user
	#The firstname and lastname fields are not required also.
	@staticmethod
	def create_prowlist_user(request):
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



	#This method gets the memeber from request, if this returns an error means that the memeber 
	#was not found, returns the member if everuthing is correct.
	@staticmethod
	def get_member_from_request(request):
		error = None
		member = None
		if 'HTTP_PROWLIST_USER' in request.META:
			try:
				token = Token.objects.get(token=request.META['HTTP_PROWLIST_USER'])
				try:
					error = None
					member = Member.objects.get(token=token)
				except Member.DoesNotExist:
					error = {
						"cod" : 102,
						"message" : "The member was not found."}

			except Token.DoesNotExist:
				error = {
					"cod" : 101,
					"message" : "The token provided is not valid."}
		else :
			error = {
				"cod" : 100,
				"message" : "No session provided."}
		return member, error

