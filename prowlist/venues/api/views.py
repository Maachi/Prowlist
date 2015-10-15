from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.core.paginator import Paginator
from members.auth.authentication import MemberAnonymous
from .. models import *
from datetime import datetime



@api_view(('GET', 'POST', ))
@permission_classes((AllowAny, ))
def near_venues(request, format=None):
	items_per_page = 2
	current_page = 1
	venues = Venue.objects.filter(active = True)
	venues_array = []
	if venues:
		for venue in venues:
			venues_array.append(venue.serialize())
	pages = Paginator(venues_array, items_per_page)
	content = {
		'pager' : {
			'total_pages' : pages.num_pages,
			'items_per_page' : items_per_page,
			'total_items': pages.count,
			'current_page' : current_page,
		},
		'items' : pages.page(current_page).object_list,
	}
	return Response(content)



@api_view(('GET',))
@permission_classes((AllowAny, ))
def venue_detail(request, format=None):
	response = {}
	try :
		venue = Venue.objects.get(pk=1)
		response = venue.serializeWithProducts()
	except Venue.DoesNotExist:
		response = {}
	return Response(response)

