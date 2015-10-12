from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^get_near_venues/', views.near_venues, name='getting-near-venues'),
]