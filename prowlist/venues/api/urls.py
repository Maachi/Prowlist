from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^near/', views.near_venues, name='getting-near-venues'),
]