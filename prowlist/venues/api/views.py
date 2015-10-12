from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from members.auth.authentication import MemberAnonymous
from .. models import *
from datetime import datetime



@api_view(('GET',))
@permission_classes((AllowAny, ))
def near_venues(request, format=None):
	content = {
		'token': "mundo...."
	}
	return Response(content)

