from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


@api_view(('GET',))
@permission_classes((AllowAny, ))
def get_products(request, format=None):
	content = {
		'hola': 'mundo'
	}
	return Response(content)