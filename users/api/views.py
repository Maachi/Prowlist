from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from .. models import *
from datetime import datetime


@api_view(('GET',))
@permission_classes((AllowAny, ))
def authenticate_device(request, format=None):
    unique_id = get_random_string(length=16, 
        allowed_chars='abcdefghijklmnopqrstuvxyz1234567890')
    email = u'{unique_id}@prowlist.com'.format(
            unique_id=unique_id)
    user = User.objects.create_user(email=email,
        password='123')
    token = Token.objects.create(user=user)
    response = {
        'token' : token.key,
        'user' : user.serialize()
    }
    return Response(response)
