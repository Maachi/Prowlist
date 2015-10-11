from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .. auth.authentication import MemberAnonymous
from .. models import *
from .. utils import *
from datetime import datetime


#This method helps to obtain the user agent from the request
def get_user_agent(request):
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
def get_device(request):
	try:
		device = Device.objects.get(client=request.META['HTTP_USER_AGENT'])
	except Device.DoesNotExist:
		device = Device()
		device.client = request.META['HTTP_USER_AGENT']
		device.platform = get_user_agent(request)
	device.save()
	return device



@api_view(('GET',))
@authentication_classes((MemberAnonymous,))
@permission_classes((AllowAny, ))
def quick_signup(request, format=None):
	member = Member()
	token = Token()
	device = get_device(request)
	token.save()
	member.token = token;
	member.join_date = datetime.now()
	member.save()
	token.devices.add(device)
	content = {
		'token': token.token
	}
	return Response(content)



@api_view(('GET',))
@permission_classes((AllowAny, ))
def me(request, format=None):
	member, error = MembersUtils().get_member_from_request(request)
	if error:
		content = error
	else:
		content = member.to_object()
	return Response(content)



@api_view(('GET', 'POST'))
@permission_classes((AllowAny, ))
def enhance_user(request, format=None):
	member, error = MembersUtils().get_member_from_request(request)
	response = None
	if not error:
		if not member.user and request.body:
			if "email" in request.body:
				user, error = MembersUtils().create_prowlist_user(request)
				if user :
					member.user = user
					member.save()
		location = MembersUtils().save_location_from_request(request)
		if location:
			member.locations.add(location)
		response = member.to_object()
	return Response(response)
