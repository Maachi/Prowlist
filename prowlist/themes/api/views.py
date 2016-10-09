from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from members.auth.authentication import MemberAnonymous
from sorl.thumbnail import get_thumbnail
from .. models import *
from datetime import datetime
import json


@api_view(('GET', 'POST'))
@authentication_classes((MemberAnonymous,))
@permission_classes((AllowAny, ))
def scale_image(request, width, height, image_path, format=None):
	image = None
	#Validate the image path format
	size = '{0}x{1}'.format(width, height)
	if image_path:
		image = get_thumbnail(image_path, size, crop='center', quality=99).url
	content = {
		'image': image
	}
	return Response(content)



