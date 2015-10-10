from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import AnonymousUser
from rest_framework import exceptions
from members.models import *
 
class MemberSessionAuthentication(BaseAuthentication):

	#Extracts the token from the original request
	def get_identifier(self, request):
		if 'HTTP_PROWLIST_USER' in request.META:
			token = request.META['HTTP_PROWLIST_USER']
			try:
				token = Token.objects.get(token=token)
				return token
			except Token.DoesNotExist:
				return None
		elif 'prowlist-user' in request.GET:
			token = request.GET['prowlist-user']
			try:
				token = Token.objects.get(token=token)
				return token
			except Token.DoesNotExist:
				return None
		return None


	#Gets the member from the token
	def get_member(self, request):
		token = self.get_identifier(request)
		if token : 
			try:
				member = Member(token=token)
				return Member
			except Member.DoesNotExist:
				return None
		return None


	def authenticate(self, request):
		# Get the underlying HttpRequest object
		request = request._request
		member = self.get_member(request)
		if member:
			if member.user :
				return (member.user, None)
			else :
				return (AnonymousUser(), None)
		else :
			if request.user and request.user.is_superuser:
				return (request.user, None)
		raise exceptions.AuthenticationFailed(u'The user is invalid or the provided token does not match.')



class MemberAnonymous(MemberSessionAuthentication):

	def authenticate(self, request):
		# Get the underlying HttpRequest object
		request = request._request
		member = self.get_member(request)
		if member:
			if member.user :
				return (member.user, None)
			else :
				return (AnonymousUser(), None)
		else :
			if request.user and request.user.is_superuser:
				return (request.user, None)
			else:
				return (AnonymousUser(), None)
