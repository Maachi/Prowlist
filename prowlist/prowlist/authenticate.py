from tastypie.authentication import Authentication
from members.models import *

class ProwlistAuthentication(Authentication):

	def is_authenticated(self, request, **kwargs):
		if 'HTTP_PROWLIST_USER' in request.META:
			token = request.META['HTTP_PROWLIST_USER']
			try:
				token = Token.objects.get(token=token)
				return True
			except Token.DoesNotExist:
				return False
		return False


	def get_identifier(self, request):
		if 'HTTP_PROWLIST_USER' in request.META:
			token = request.META['HTTP_PROWLIST_USER']
			try:
				token = Token.objects.get(token=token)
				return token.token
			except Token.DoesNotExist:
				return ''
		return ''