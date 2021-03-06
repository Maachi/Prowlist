from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from django.core.paginator import Paginator
from .. models import *
from .. sandbox.security import *
from datetime import datetime


@api_view(('GET',))
@permission_classes((IsAuthenticated, ))
@authentication_classes((TokenAuthentication, ))
def get_active_products(request):
    response = {}
    items_per_page = request.GET.get('items_per_page', 2)
    current_page = request.GET.get('page', 1) 
    products_response = []
    products = Product.objects.filter(active=True)
    paginator = Paginator(products, items_per_page)
    if paginator:
        response['num_pages'] = paginator.num_pages
        response['items_per_page'] = items_per_page
        response['current_page'] = current_page
        for product in paginator.page(current_page):
            products_response.append(product.serialize())
    response['produts'] = products_response
    return Response(response)



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
def purchases(request, format=None):
    response = []
    purchases = Purchase.objects.all()
    for purchase in purchases:
        response.append(purchase.serialize())
    return Response(response)



@api_view(('GET',))
@permission_classes((AllowAny, ))
def buy_product(request, product_id, format=None):
    response = {}
    product = None
    status = 200
    try :
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        status = 404
        response = {}
    if member and product :
        #This is a asynchronous process, we need to evaluate a micro service implementation here, 
        #for this phase we have make this process available for every member
        sandbox = Security(product_id, member.token.token)
        #Starting asynch process
        if sandbox.validate():
            purchase = Purchase()
            purchase.member = member
            purchase.product = product
            purchase.save()
            response = {'purchase' : purchase.serialize()}
        else:
            status = 500
            response = {'error' : sandbox.raise_error()}
    else :
        response = {}
    return Response(response, status=status)