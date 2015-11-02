from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^scale/(?P<width>\d+)x(?P<height>\d+)/(?P<image_path>.*)', views.scale_image, name='scale-image'),
]