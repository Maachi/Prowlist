from tastypie.http import HttpForbidden, HttpApplicationError
from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.utils import trailing_slash
from prowlist.authenticate import *
from django.conf.urls import url
from datetime import datetime
from members.models import *
from members.utils import *
import base64
import json


class MembersResource(ModelResource):
	class Meta:
		queryset = Member.objects.all()
		allowed_methods = ['get', 'post']
		resource_name = 'members'
		excludes = ['password', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'resource_uri']
		authentication = ProwlistAuthentication()
		authorization = DjangoAuthorization()

	#Lets override the urls in order to have more control
	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/login%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('login'), name="api_login"),
			url(r'^(?P<resource_name>%s)/logout%s$' % (self._meta.resource_name, trailing_slash()), self.wrap_view('logout'), name='api_logout'),
			url(r"^(?P<resource_name>%s)/quick-signup%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('signup'), name="api_login"),
			url(r"^(?P<resource_name>%s)/update%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('enhance_user'), name="api_enhance_user"),
			url(r"^(?P<resource_name>%s)/me%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('me'), name="api_get_user_session"),			
		]


	#This method helps to obtain the user agent from the request
	def get_user_agent(self, request):
		agent = request.META.get('HTTP_USER_AGENT', '').lower()
		user_client = ""
		if agent.find("iphone") > 0 or agent.find("ipad") > 0 or agent.find("ipod") > 0:
			user_client = "ios"
		elif agent.find("android") > 0 or agent.find("java") > 0:
			user_client = "android"
		else:
			user_client = "browser"
		return user_client


	#Saves the device in a secure manner
	def get_device(self, request):
		try:
			device = Device.objects.get(client=request.META['HTTP_USER_AGENT'])
		except Device.DoesNotExist:
			device = Device()
			device.client = request.META['HTTP_USER_AGENT']
			device.platform = self.get_user_agent(request)
		device.save()
		return device


	def signup(self, request, **kwargs):
		self.method_check(request, allowed=['get', 'post'])
		member = Member()
		token = Token()
		device = self.get_device(request)
		token.save()
		member.token = token;
		member.join_date = datetime.now()
		member.save()
		token.devices.add(device)
		return self.create_response(request, {
			"token" : token.token
		})

	#This api method allows to save different user information
	def enhance_user(self, request, **kwargs):
		self.is_authenticated(request)
		self.method_check(request, allowed=['post'])
		member, error = MembersUtils.get_member_from_request(request)
		if error:
			return self.create_response(request, error, HttpApplicationError)
		else:
			if not member.user and request.body:
				if "email" in request.body:
					user, error = MembersUtils.create_prowlist_user(request)
					if user :
						member.user = user
						member.save()
			location = MembersUtils.save_location_from_request(request)
			if location:
				member.locations.add(location)
			return self.create_response(request, member.to_object())


	#This services returns the user information, this is an open window to check if the user is valid or not
	def me(self, request, **kwargs):
		self.is_authenticated(request)
		self.method_check(request, allowed=['get', 'post'])
		member, error = MembersUtils.get_member_from_request(request)
		if error:
			return self.create_response(request, error, HttpApplicationError)
		else:
			return self.create_response(request, member.to_object())


