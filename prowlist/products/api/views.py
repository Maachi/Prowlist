from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.core.paginator import Paginator
from .. models import *
from .. sandbox.security import *
from datetime import datetime


@api_view(('GET',))
@permission_classes((AllowAny, ))
def product_detail(request, product_id, format=None):
	response = {}
	try :
		product = Product.objects.get(pk=product_id)
		response = product.serialize()
	except Product.DoesNotExist:
		response = {}
	return Response(response)



@api_view(('GET',))
@permission_classes((AllowAny, ))
def buy_product(request, product_id, format=None):
	response = {}
	return Response(response)