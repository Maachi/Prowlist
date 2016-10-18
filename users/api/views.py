from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from django.core.paginator import Paginator
from .. models import *
from datetime import datetime




@api_view(('POST',))
@permission_classes((AllowAny, ))
def create_client_user(request, product_id, format=None):
    response = {}
    return Response(response)
