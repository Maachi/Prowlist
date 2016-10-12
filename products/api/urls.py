from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<product_id>\d+)/$', views.product_detail, name='getting-product-detail'),
	url(r'^(?P<product_id>\d+)/buy/$', views.buy_product, name='buy-product'),
	url(r'^purchases/$', views.purchases, name='purchases'),
]