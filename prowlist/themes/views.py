from django.shortcuts import render
from django.http import HttpResponse
from sorl.thumbnail import get_thumbnail

def scale_image(request, width, height, image_path):
	image = None
	#Validate the image path format
	size = '{0}x{1}'.format(width, height)
	image = get_thumbnail(image_path, size, crop='center', quality=99)
	return HttpResponse(image.read(), content_type="image/jpg")