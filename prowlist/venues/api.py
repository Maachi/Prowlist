from tastypie.http import HttpForbidden, HttpApplicationError
from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.utils import trailing_slash
from prowlist.authenticate import *
from django.conf.urls import url
from datetime import datetime
from venues.models import *
from members.utils import *
import base64
import json


class VenuesResource(ModelResource):
	class Meta:
		queryset = Venue.objects.all()
		allowed_methods = ['get', 'post']
		resource_name = 'venues'
		#excludes = ['password', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'resource_uri']
		authentication = ProwlistAuthentication()
		authorization = DjangoAuthorization()

	#Lets override the urls in order to have more control
	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_venues'), name="api_venues"),
			url(r"^(?P<resource_name>%s)/(?P<venue_id>\d+)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_venue'), name="api_venue"),
			url(r"^(?P<resource_name>%s)/(?P<venue_id>\d+)/products%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_products_by_venue'), name="api_products_venue"),		
		]


	def get_products_by_venue(self, request, **kwargs):
		products = []
		try:
			venue = Venue.objects.get(pk=kwargs['venue_id'], active=True)
			if venue.products:
				for product in venue.products.all():
					if product.active:
						product_object = product.to_object()
						products.append(product_object)
		except Venue.DoesNotExist:
			self.create_response(request, products)
		return self.create_response(request, products)


	def get_venues(self, request, **kwargs):
		self.is_authenticated(request)
		self.method_check(request, allowed=['post', 'get'])
		venues = Venue.objects.filter(active=True)
		venues_response = []
		for venue in venues:
			venues_response.append(venue.to_object())
		return self.create_response(request, venues_response)



	def get_venue(self, request, **kwargs):
		self.is_authenticated(request)
		self.method_check(request, allowed=['post', 'get'])
		venue = None
		try:
			venue = Venue.objects.get(pk=kwargs['venue_id'], active=True)
			venue_object = venue.to_object()
			return self.create_response(request, venue_object)
		except Venue.DoesNotExist:
			self.create_response(request, venue)
		return self.create_response(request, venue)



