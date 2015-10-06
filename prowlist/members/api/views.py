from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .. auth.authentication import MemberAnonymous
from rest_framework.response import Response


@api_view(('GET',))
@authentication_classes((MemberAnonymous,))
@permission_classes((AllowAny, ))
def quick_signup(request, format=None):
	content = {
		'hola': 'mundo cruel'
	}
	return Response(content)