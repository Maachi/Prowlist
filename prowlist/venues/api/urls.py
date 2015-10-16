from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^near/', views.near_venues, name='getting-near-venues'),
	url(r'^(?P<venue_id>.*)$', views.venue_detail, name='getting-venue-detail')
]