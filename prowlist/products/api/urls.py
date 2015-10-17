from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<product_id>.*)$', views.product_detail, name='getting-product-detail')
]